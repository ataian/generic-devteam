# Optional offline export

Only on an explicit additional assignment. Not part of the standard delivery and no bypass of the project rules.

## One implementation, additional output

Export from the same components, data, and compiled styles as the regular view. Reuse the existing build/render path; do not maintain a second HTML/framework stack. If interactions are commissioned, preserve and check their offline capability separately; a static export must not silently lose them.

Embed all required styles, images, original assets, and fonts. No CDN calls, external imports, relative file dependencies, hidden fetches, or dependency on service-worker/browser cache. Path check and an actual offline browser complement each other. Check not only visible img sources, but also CSS URLs, fonts, imports, and scripts.

## Repeatable and failure-safe run

1. Validate inputs/state and expected assets; prepare the output separately first.
2. Produce the export with an unambiguous success/error status. Publish it as the current result only after a successful check. A missing original asset is an error, not an automatic substitute graphic.
3. If an old export exists, a failed run must neither present it as new nor offer it through a stale success marker. Leave the old state identifiable; required file removal is subject to the existing rights.
4. Check a repeated export of the same state. If timestamps or similar produce differences, document the cause and a reproducible comparison basis, do not claim byte equality unchecked.

## Actual offline acceptance

Open the finished single file in the browser via `file://` in isolation, without neighbouring files and without a usable network connection, and without helpful old caches. A server call with embedded styles alone is not enough.

Check the commissioned viewports: content, images/original assets, fonts, long texts, missing values, and commissioned interactions. Actually look at the source, the regular browser render, and the offline view. Run the missing-asset probe with an existing old export: the error must be visible, the old export must not become a current success.

The handoff names the export path/state, the repeatable generation path, real positive and negative results, offline/visual evidence, and open limits. Without these checks, export acceptance stays open; deployment does not follow from it automatically.
