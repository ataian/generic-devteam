# Visual comparison

## Comparison conditions first

Record in the existing brief or check log:

- commissioned CSS viewport per target size, browser zoom, and pixel density (DPR);
- source including page/section, scaling, and crop; visible viewport or full page;
- data state including long-text/missing-value cases, fonts, and accepted substitute fonts;
- approved content/color/layout deviations and agreed acceptance criteria;
- work budget and remaining render/correction attempts.

A PDF page has no implicit browser viewport. With unknown pixel density, an image width must not be halved across the board. Clarify relevant unknown conditions, do not invent fitting values.

## Real capture and check

1. Actually build/start with an approved project tool. Make load errors, wrong data, auth/mock mode, and browser errors visible. No unapproved operations change to start it.
2. Wait for finished content, images, and fonts, not only for the first DOM build-up or an arbitrary sleep. Use available readiness signals such as completed data queries, image decoding, and font readiness.
3. Create captures for the commissioned scope. **Look at the source and the actual render.** A saved image, DOM text, or a pixel diff alone is not complete visual evidence.
4. Compare in this order: content/completeness and structure; grid/alignment; spacing; typography/line breaks; colors; assets/details. Approved differences are part of the target state.
5. Check long texts, variable lists/extras, and contractually distinct null/missing/empty/0 cases. No omission as a layout fix. Do not excuse unintended overflow, clipping, or overlaps as a font fallback.
6. Check semantics, alternative texts, labels, and contrast; for interactions, exercise visible focus and keyboard operation. Clarify concrete conflicts with template fidelity. No unrestricted accessibility claim from a visual check.
7. Correct deviations in a targeted way and re-check the affected conditions. Run the prescribed project checks in addition; render capability alone is no behaviour/contract acceptance.

## Honest stop logic

Prescribe no universal number of passes and no blanket pixel-diff threshold. The agreed budget limits attempts, not the acceptance quality.

- Browser/build missing: render evidence open; other independent checks may continue.
- Image view missing: technical capture possibly evidenced, visual match **not checked**.
- Budget exhausted: no further automatic round; hand over remaining differences, impacts, and missing evidence. Do not present as passed through wording.

The evidence names source, code/build state, data and comparison conditions, real captures/test results, differences considered, accepted deviations, and open defects. Mark external reports as such, not as your own execution.
