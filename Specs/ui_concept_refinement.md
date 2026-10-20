# Concept fidelity pass

Reference: `Design/UI_Review_v1/` with the map and messaging corrections in `Design/UI_Review_v2/`.

## Changes

- Noto Serif interface typography, matching the literary concept treatment.
- Rounded translucent brown panels, antique-gold outer rims and subdued inner rims; pill-shaped primary menu and travel buttons.
- Native line-art medallions for library categories and phone apps, replacing unrelated Unicode symbols.
- Vietnamese calligraphic title artwork, preserving live English title fallback.
- Map retains existing city artwork and coordinates. Detail card now occupies the map column, with a location preview and inset travel control. Sidebar extends alongside that card.
- Phone has an ornamental rounded shell, gold dividers, consistent message bubbles and separate reply choices.
- Profile list uses portrait medallions; detail header has a larger portrait, title and divider.
- Library and profiles separate the sidebar and content into independent rounded panels, over a lightly softened background.

## Raster assets

Generated with the built-in image generation tool; originals preserved. Runtime copies are in `game/gui/theme/refined/`:

- `gold_botanical_corner.png`: RGBA, 1254×1254. True transparent background plus partially transparent edge pixels. Displayed at restrained opacity in ornamental panels.
- `title_vi.png`: RGBA, 1774×887. True transparent background and partially transparent gold glow. Vietnamese menu title only.

Final prompts:

> Use case: stylized-concept. Production game UI ornament asset on genuine transparent alpha background. Single delicate antique gold botanical corner flourish: graceful slender curved branch with six narrow leaves, tiny filigree curls. Matches warm brown and cream romantic visual novel interface. Composition: ornament entirely in lower-right corner of square canvas, extending along bottom and right edges, center and upper-left completely transparent. Fine crisp engraved gold lines, restrained soft warm highlights, no opaque background, no checkerboard, no text, no frame, no shadow rectangle. Asset will be overlaid at 150px in UI panels. Save output image for use in local project.

> Use case: logo-brand. Asset type: transparent title lettering for a Vietnamese romantic visual novel. Exact text on two lines: "Tựa gió," then "tựa mây". Elegant thin high contrast copperplate calligraphy, sweeping graceful uppercase T and long understated swashes, highly readable accurate Vietnamese diacritics. Warm ivory lettering with subtle champagne gold edge glow. Wide horizontal composition, text fully contained with generous transparent margin. Only the words, no leaves, no objects, no background, no checkerboard, no watermark. Genuine transparent alpha channel. Match literary romantic evening rainy-window atmosphere. This is final game title art, not a mockup.

## Fidelity boundaries

Concepts are references, not flattened screen overlays. Text, unlocked data, travel actions, scrolling and language switching stay native. Main menu retains its existing rainy-window background; Library, Phone and the space around the city map use the clean cafe plate added in revision 2. City map artwork and coordinates are unchanged. Assets are stylistic approximations, not exact extractions from the concept. Existing narrative strings are unchanged.

## Verification

Native Windows Ren'Py UI suite covers English/Vietnamese at 1920×1080 and 1280×720, with 36 assertions covering screen navigation and locked travel. Review captures are in `tests/screenshots/ui_refresh/`. Asset pixel inspection confirms both PNGs use 32-bit ARGB with fully transparent and partially transparent pixels. Ren'Py lint exits 0, with the same existing story sprite/speaker warnings. Unrelated staged optimizer changes and untracked concept/reference files are preserved.

## Revision 2 — smooth materials and restrained ornament (2026-10-20)

- Replaced low-resolution integer polygon panel borders with an analytic rounded-rectangle GPU shader. Signed-distance coverage is antialiased in physical-pixel units, including 720p windows. Fill and stroke are premultiplied-alpha composited. A quiet inner rim is reserved for ornamental shells, not doubled on every card.
- Removed the angular corner/diamond decorations and the old baroque botanical raster from panel rendering. Ornaments are now explicit, sparse screen elements, kept clear of controls.
- Added eight editable SVG icons (person, book, music, gallery, extras, gamepad, leaf and settings), rasterized at 4× with filtered scaling. Other native line artwork and map pins are supersampled too. Map pin symbols now distinguish building/home/plane/cup where the location id provides that information.
- Enlarged Library category medallions to 112 logical pixels, shortened its navigation panel, restored the quote area, and fixed footer arrows to the right edge of each card.
- Rebalanced cafe glass opacity and warm border tones. Phone reply text is larger, reply choices have more room, and back controls are circular.
- Map navigation actions moved into the header; sidebar ornament occupies the vacated bottom area. Travel CTA remains inset inside the map detail frame. English Timeline label fits on one line.
- Corrected Vietnamese Extras/Original Stories labels and added the missing CG translations; no story prose changed.

Selected new project assets, generated using the built-in image tool:

- `game/gui/theme/refined/botanical_sprig_v2.png`: 1254×1254 RGBA. Alpha sampling found 29,204 fully transparent and 3,195 semi-transparent samples. Used with restrained opacity; original generated image preserved.
- `game/gui/theme/refined/rainy_library_v2.png`: 1672×941 RGB background plate, reconstructed from the Phone concept without baked-in UI. Used behind Library/Phone and around (not instead of) the existing city map.
- `game/gui/theme/refined/icon_*.svg`: eight code-authored vector assets, not AI-generated bitmaps.

Final selected generation prompts:

> Use case: stylized-concept. Production transparent PNG overlay asset for an elegant Vietnamese literary visual novel UI. Reference image 1 is STYLE REFERENCE ONLY: match the extremely delicate antique gold botanical sprig at the bottom right of its map sidebar. Generate ONE single slender curved leafy sprig, on genuine transparent alpha, no UI panel or background. Branch sweeps gently from lower left toward upper right, with 7 to 9 elongated pointed leaves alternating organically. Leaves are hollow outlines with a single fine vein, not solid chunky leaves. Restrained fine copperplate penwork, champagne/antique gold (#b8935e) with gentle tonal variation, crisp anti-aliased edges, understated matte metallic finish, no glitter, no bloom or glow. Balanced sparse silhouette fitting in a square with 8 percent margins. It must feel like an elegant botanical engraving on a book cover, NOT baroque filigree, NOT arabesque, NOT ornate curls. No text, no border, no diamonds, no extra objects. The rest of canvas must be fully transparent. Final asset will be displayed at 140-200 pixels.

> Use case: precise-object-edit. Asset type: clean 16:9 game background plate, with absolutely no UI. Input image 1 is the target scene and style reference. Remove the entire smartphone UI overlay from the center and reconstruct the cozy rainy-night cafe/library interior behind it seamlessly. Preserve the beautiful painterly semi-realistic cinematic visual novel rendering, warm brown timber, blue rain-streaked large windows, warm table lamp on left, flowers and porcelain cup, books and notebook on wooden table at bottom, floor lamp and leafy plant at upper right, bookcases on right. Behind the removed center panel show the continuous rainy window panes and softly lit cafe interior, not another phone. Balanced warm amber highlights against cool desaturated blue night. Center and right-center should have low contrast details, suitable for overlaying translucent UI. No people. No text, no lettering, no logos, no icons, no borders, no decorative UI, no screen, no controls. Edge-to-edge finished background artwork, 16:9 landscape, high detail without oversharpening. Keep the composition of the reference as closely as possible.

A generated Map lettering variant was rejected for excessive emboss/glow and was not copied into the project or used at runtime. The existing native italic heading remains. Older botanical PNG is preserved but no longer referenced by UI code.

Validation: iterative native Windows screenshots, followed by the final English/Vietnamese × 1080p/720p UI run (44 assertions, including CG/Extras translation checks and active-day Map coverage). Active-day captures are named `10_map_active_*`; they exercise the Today summary and all four header controls. Lint exits 0 with the same 29 pre-existing story sprite/speaker warnings. These checks establish runtime/navigation health, not pixel-identical concept fidelity; review the actual captures in `tests/screenshots/ui_refresh/`.
