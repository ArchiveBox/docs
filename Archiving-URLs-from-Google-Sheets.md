# Archiving URLs from Google Sheets

Save a spreadsheet and the pages linked inside it. Start with a running [ArchiveBox server](Quickstart) with Chrome installed.

*Requires the development build with saved-document discovery in `parse_txt_urls`.*

## 1. Put your links in a sheet

Use ordinary URLs or linked cell text, in any column. This example uses Andrew Wheeler's public [research replication materials](https://docs.google.com/spreadsheets/d/1g8eYhbeu55Z5rLpvRSjdPZVVYYBq5gSb4Isl6vmcAa0/edit).

![Google Sheet with links to papers, GitHub repositories, and datasets](screenshots/google-sheets/01-source-sheet.jpg)

## 2. Add the sheet URL

Open **Add** in ArchiveBox. Paste the sheet's URL and select **depth = 1**. Keep the default plugins enabled and leave **Same domain only** unchecked.

![One Google Sheet URL with archive depth set to 1](screenshots/google-sheets/02-add-sheet.jpg)

For a private sheet, select a [Persona with your Google login session](Chromium-Install#setting-up-a-chromium-user-profile).

Click **Create Crawl and Start Archiving**.

## 3. Open the saved pages

Open **Snapshots**. Search for a domain from your sheet and press **Enter**. The discovered URLs appear automatically; open a result once archiving finishes to browse its saved copies.

![Links from the sheet queued automatically with the default plugins](screenshots/google-sheets/03-discovered-links.jpg)

All URL parsers run, so the crawl can also include links from Google's surrounding UI.

The same steps work with a Google Doc containing links: paste its document URL and select **depth = 1**.

## 4. Optional: write results back to the sheet

Use a sheet you can edit. Add columns beside the original URLs, such as **Snapshot**, **Screenshot**, and **Status**.

### A. Automatic: ask the built-in AI agent

Enable `OPENCODE_ENABLED=True`, restart ArchiveBox, then open **Agent** as an admin and connect your AI provider. Give it the sheet URL, your Persona name, and the columns to fill:

> Update [sheet URL] with the results from crawl [crawl ID]. Use the Google login cookies from my “Research” Persona to edit the sheet in Chrome. Match the original URLs in column A; put each snapshot detail-page link in B, its saved screenshot link in C, and the capture status in D. Only update those result columns. Check the saved outputs before marking a row complete, and leave unavailable screenshots blank.

The Persona's Google account needs editing access. This is an agent task you request after archiving; repeat it for later captures.

### B. Manual setup: webhooks → n8n → Google Sheets

For ongoing updates, [n8n](https://n8n.io/integrations/webhook/and/google-sheets/) provides a visual workflow:

**Webhook → If finished → HTTP Request → Google Sheets: Update Row**

1. In n8n, create a **POST Webhook** with Header Auth. In ArchiveBox's **Admin → Outbound Webhooks**, select model `archivebox.core.models.Snapshot`, signal **Update**, and paste the webhook's production URL and matching authentication header. Publish the n8n workflow.
2. In the **If** node, require `body.fields.status` to equal `sealed`, and `body.fields.crawl` to equal your sheet's crawl ID. A sealed snapshot has finished processing; individual outputs may still have failed.
3. Use **HTTP Request** to fetch `/api/v1/core/snapshot/{body.pk}` from your ArchiveBox API origin, with an ArchiveBox API key in `X-ArchiveBox-API-Key`. The response includes `url`, `archive_path`, and `archiveresults` with saved `output_files`.
4. Connect Google Sheets and choose [**Update Row**](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations/#update-row). Match your original URL column against `url`; map only your result columns. Build **Snapshot** from your ArchiveBox web origin + `/` + `archive_path`, and **Screenshot** from that link + `#screenshot/screenshot.png` when the screenshot output exists. Other saved outputs use their corresponding file path after `#`.

Use a column containing the literal URL for matching. Updating existing rows also makes repeated webhook deliveries harmless. n8n must be able to reach your ArchiveBox API; readers need access to its saved pages. Screenshot links open the saved image in ArchiveBox.

## Other tools

- [Bellingcat Auto Archiver](https://www.bellingcat.com/resources/2022/09/22/preserve-vital-online-content-with-bellingcats-auto-archiver-tool/) — reads URLs from Google Sheets and writes archive status and locations back. [Google Sheets setup](https://auto-archiver.readthedocs.io/en/latest/how_to/02_gsheets_setup.html).
- [Wayback Machine: Save Page Now for Google Sheets](https://archive.org/services/wayback-gsheets/) — submit a sheet of URLs to archive in the Internet Archive.
