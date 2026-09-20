Use a Slack bot to save links posted in a channel and announce newly added snapshots. [n8n](https://n8n.io/) connects Slack's Events API to ArchiveBox's REST API, and turns ArchiveBox's outbound webhooks into Slack messages.

```text
📥 #save-links → Slack Trigger → extract URLs → ArchiveBox API → collection
📣 collection → Snapshot Create webhook → n8n → #archive-updates
```

See below for intructions to set up two common workflows:

- one to collect URLs for saving
- one to announce new URLs added to the collection in a channel

## 1. Prepare ArchiveBox and Slack

- Run an [ArchiveBox server](https://github.com/ArchiveBox/ArchiveBox/wiki/Quickstart) with its background archiving worker/orchestrator running. API additions queue work; a successful request alone does not mean extraction has finished.
- In ArchiveBox, open **Admin → API Keys** (`/admin/api/apitoken/`) and create a key owned by a superuser. The current REST API requires superuser credentials. Store it in an n8n **Header Auth** credential with the name `X-ArchiveBox-API-Key`.
- Run n8n with a persistent database. Its Slack Trigger needs a public HTTPS URL reachable by Slack; n8n must also reach your ArchiveBox API. ArchiveBox can remain private if n8n can reach it over your internal network or VPN.
- Create a Slack app at [Your Apps](https://api.slack.com/apps), install it in your workspace, and invite its bot to `#save-links` and `#archive-updates` (choose your own channels).

For a public input channel, add bot scopes `channels:history`, `channels:read`, `groups:read`, and `users:read`. The read scopes support the n8n trigger's channel/user lookup controls; `groups:read` covers its combined public/private channel lookup. Add `groups:history` if the input channel is private, and `chat:write` for posting announcements. Reinstall the app after changing scopes. See [Slack message subscriptions](https://docs.slack.dev/reference/events/message.channels/) and [n8n Slack credentials](https://docs.n8n.io/integrations/builtin/credentials/slack/).

Use the bot's `xoxb-…` token in n8n's Slack API credential. Also set its **Signature Secret** from Slack **Basic Information → Signing Secret**; n8n's Slack Trigger supports signature verification from version 1.106.0 onward. Keep both tokens in credentials, not workflow code or channel messages. [Slack Trigger documentation](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger/).

## 2. Ingest new URLs from Slack

Build this n8n workflow:

```text
Slack Trigger → Code: extract URLs → deduplicate message → HTTP Request: add URLs
```

### Configure the trigger

Select **New Message Posted to Channel**, turn **Watch Whole Workspace** off, and select the input channel. Leave **Resolve IDs** off. In the Slack app's **Event Subscriptions**, use this trigger's webhook URL and subscribe to `message.channels` (or `message.groups` for a private channel). After testing, switch Slack to the node's **Production URL** and publish/activate the workflow. Slack accepts one Events API request URL per app; the test URL and production URL are different. [n8n configuration](https://docs.n8n.io/integrations/builtin/credentials/slack/#slack-trigger-configuration).

### Extract links and prevent loops

Add a **Code** node in **Run Once for All Items** mode. Replace the channel ID below with your input channel's ID. The Slack Trigger emits the inner event directly, so its message text is `$json.text`, not `$json.event.text`. This filter handles ordinary user messages, ignores edits/deletions and bot messages, and keeps HTTP(S) links only. [Trigger output implementation](https://github.com/n8n-io/n8n/blob/master/packages/nodes-base/nodes/Slack/SlackTrigger.node.ts).

```javascript
const inputChannel = 'C0123456789';
const output = [];
for (const item of $input.all()) {
  const e = item.json;
  if (e.type !== 'message' || e.channel !== inputChannel ||
      e.bot_id || e.app_id || e.subtype || !e.user || !e.ts) continue;

  // Slack normally encodes links as <https://example.com|label>.
  const text = String(e.text || '')
    .replace(/<(https?:\/\/[^>|]+)(?:\|[^>]*)?>/g, '$1')
    .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>');
  const urls = [...new Set(text.match(/https?:\/\/[^\s<>]+/g) || [])]
    .filter(url => /^https?:\/\/[^/?#@\s]+(?:[/?#]|$)/i.test(url));
  if (!urls.length) continue;
  output.push({json: {
    messageKey: `${e.channel}:${e.ts}`,
    urls,
    tag: 'slack',
  }});
}
return output;
```

ArchiveBox validates the submitted URLs. The parser preserves query strings and fragments; it deliberately avoids guessing whether trailing punctuation belongs to a URL. Prefer Slack's formatted links and inspect your first real execution. Restrict the bot to trusted users/channels: HTTP(S) validation alone does not prevent requests to private network addresses. Use network isolation or a domain allowlist when accepting untrusted submissions. Keep the output channel separate and retain the bot-message filter even if you later combine channels.

Slack can redeliver events. Before the API call, use a persistent store to check `messageKey`; skip keys already successfully submitted and record success afterward. For a small, sequential workflow, n8n's [Data Table node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/) can look up and insert these keys. Concurrent/high-volume workflows need an atomic unique-key claim in a database or queue; a lookup followed by insert is not atomic. A crash between the API call and recording success can still replay a submission, so this is not an exactly-once guarantee.

### Call the ArchiveBox API

Configure an **HTTP Request** node:

| Setting | Value |
| --- | --- |
| Method | `POST` |
| URL | `https://YOUR-ARCHIVEBOX-ADMIN-HOST/api/v1/cli/add` |
| Authentication | Generic Credential Type → Header Auth → your ArchiveBox credential |
| Body content type | JSON |
| JSON body (expression) | `{{ { urls: $json.urls, tag: 'slack', depth: 0, only_new: true } }}` |

Require both an HTTP success status and `success: true` in the response before recording the message key. Preserve the key from the upstream Code node; the HTTP response replaces the current item's JSON. Keep failed executions available for review/replay.

A standalone request with the same shape is:

```bash
curl --fail-with-body \
  -H "X-ArchiveBox-API-Key: $ARCHIVEBOX_API_KEY" \
  -H 'Content-Type: application/json' \
  --data '{"urls":["https://example.com/"],"tag":"slack","depth":0,"only_new":true}' \
  'https://YOUR-ARCHIVEBOX-ADMIN-HOST/api/v1/cli/add'
```

`only_new` controls archiving behavior; it does not replace deduplicating Slack deliveries. The current API returns `success`, `errors`, and `result` containing `crawl_id`, `num_snapshots`, `snapshot_ids`, and `queued_urls`. Background parsing can leave `snapshot_ids` initially empty. Do not treat this response as an extraction-complete notification. [API implementation](https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/api/v1_cli.py), [authentication](https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/api/auth.py).

## 3. Announce additions to the collection

Build a second n8n workflow:

```text
Webhook (POST, Header Auth) → validate snapshot → deduplicate snapshot ID → Slack: send message
```

Create a **Webhook** node with method `POST`, an arbitrary path such as `archivebox-snapshot-created`, and **Header Auth**. Choose a new shared secret and header name such as `X-ArchiveBox-Webhook-Secret`; this is separate from your ArchiveBox API key. Select **Respond Immediately** so ArchiveBox is not held waiting for Slack, and use the node's Production URL when the workflow is published/active. [n8n Webhook documentation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/).

In ArchiveBox, open **Admin → API Outbound Webhooks → Add** (`/admin/api/outboundwebhook/add/`):

| Field | Value |
| --- | --- |
| Name | `Slack: new snapshots` |
| Signal | **Create** (`CREATE`) |
| Referenced model | **Snapshots** (`archivebox.core.models.Snapshot`) |
| Endpoint | n8n Webhook Production URL |
| Headers | `{"X-ArchiveBox-Webhook-Secret":"YOUR-SHARED-SECRET"}` |
| Authentication token | Leave empty; this recipe uses the custom header above |
| Enabled | Checked |
| Keep last response | Optional; useful during setup |

ArchiveBox sends a JSON model record. A shortened example is:

```json
{
  "model": "core.snapshot",
  "pk": "SNAPSHOT-UUID",
  "fields": {
    "url": "https://example.com/",
    "timestamp": "1790000000.000000",
    "title": null
  }
}
```

In n8n this is under `$json.body`: require `body.model === 'core.snapshot'`, a nonempty `body.pk`, and an HTTP(S) `body.fields.url`. Use `body.pk` as the persistent notification deduplication key; keep the same concurrency/crash limitations described above in mind. Do not key announcements solely by URL: different snapshots can legitimately have the same URL.

Configure a **Slack** node to send a message to `#archive-updates` with text such as:

```text
Added to ArchiveBox: {{ $json.body.fields.url }}
```

Keep the Webhook item available if intermediary nodes replace its data. Disable link/media unfurls if desired. Record the snapshot key only after the Slack node succeeds. If using an HTTP Request instead of the Slack node, call [`chat.postMessage`](https://docs.slack.dev/reference/methods/chat.postMessage/) with a bot bearer token, `channel`, and `text`; check the JSON `ok` field as well as HTTP status.

**“Added” means the snapshot was created in the collection.** Internally this is a model **Create** signal, sometimes described informally as “snapshot created”; there is no literal `snapshot.created` event-name field in this payload. The title and extracted files may not exist yet. An **Update** subscription can fire many times and does not by itself mean archiving succeeded. This recipe intentionally announces creation, not completion. [Webhook settings](https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/core/settings.py), [admin fields](https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/api/admin.py), [payload serialization](https://github.com/MrThearMan/django-signal-webhooks/blob/main/signal_webhooks/serializers.py).

You can replace the Slack node with a request to a [Slack incoming webhook](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/) using a `{"text":"…"}` body. Keep n8n (or another adapter) between the services: ArchiveBox's raw model payload is not Slack's message schema.

## 4. Verify and operate it

1. Post a fresh HTTP(S) URL in the input channel. Inspect the n8n execution and API response; verify the URL appears in ArchiveBox and the `slack` tag is applied.
2. Verify one “Added to ArchiveBox” message appears in the output channel. Confirm that this bot message does not trigger another ingestion.
3. Add a different URL through the ArchiveBox web UI or CLI. It should produce an announcement without a Slack input message.
4. Edit the original Slack message and post a message without URLs. Neither should create another API request with the filter above.
5. Check that the orchestrator processes queued work and inspect actual saved output separately from the creation announcement.

ArchiveBox sends these webhooks after the database transaction commits. Its current handler logs delivery failures; it is not a durable retry queue. In the webhook admin, check **Last success**, **Last failure**, and optionally **Last response**. A successful immediate n8n response proves receipt, not a successful Slack post: monitor n8n failures too, and replay failed downstream executions after resolving the error. For guaranteed eventual announcements, add periodic API reconciliation against your persistent notification store. [Delivery handler](https://github.com/ArchiveBox/ArchiveBox/blob/dev/archivebox/api/webhooks.py).

A `401`/`403` from ArchiveBox usually means an absent/expired key or a key whose owner is not a superuser. A Slack trigger that only works while testing usually still has the Test URL registered. Missing webhook announcements can mean the webhook is disabled, the model/signal is wrong, n8n cannot be reached, or a bulk database operation bypassed Django's normal save signals.
