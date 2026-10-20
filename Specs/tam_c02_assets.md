# Chapter 2 scene illustrations

Generated with built-in ImageGen. Ten new CGs and one boutique background cover
all seven narrative scenes, retaining the existing premium-dress party entrance
CG. Assets live under `game/images/assets/{cg,bg}/`, opaque 1920x1080 WebP,
quality 94 with Lanczos fit. Full prompts, ordered references and generation IDs
are recorded in `tam_c02_asset_prompts.json`.

## Identity, wardrobe and framing

Character portraits in `game/images/characters/{tam,huyen,quan,hoang}/expressions/`
are identity references. The approved chapter-one collar CG supplies the updated
Huyen identity and shared semi-realistic rendering. Quan is the older stern man
in a dark shirt, distinct from Quang. Hoang has his own portrait and wears the
light shirt described at the party. Extras are blurred or viewed from behind.

Daytime Tam: white blouse and beige skirt. Daytime Huyen: powder-blue shirt and
charcoal trousers. Party Tam: existing blush beaded spaghetti-strap gown for the
premium branch, muted sage tailored short-sleeve dress for the new-office branch,
plain beige-taupe elbow-sleeve dress for the default branch. Party Huyen wears a
light jade-green dress with sheer short puff sleeves and a small pendant.
Look at scene partners or actions, not the camera. Reframe the document, model
and napkin shots so the central action clears the dialogue box.

## Integration cues

Names below use the `cg_tam_c02_` prefix.

| Image | Show / cleanup |
| --- | --- |
| `onboarding` | Tam peels the pen sticker; restore office before preparation menu. |
| `quan_document` | Actual first sight of Quan tapping the document, after the rumor menu; restore office when he puts it down and leaves. |
| `first_salary` | Huyen leans over to see Tam's phone; restore office before Tam switches off the screen. |
| `shopping` | Both still in work clothes, considering the mannequin before buying; restore boutique before purchase menu, including retry/fallback paths. |
| `party_office`, `party_default` | Respective outfit branches alongside existing `party_premium_dress`; common cleanup already restores the ballroom. |
| `hoang_model` | Hoang adjusts the blank name card; restore ballroom before approaches and menus. |
| `party_end_premium`, `party_end_office`, `party_end_default` | Match the same outfit-flag precedence as party entry. Tam adjusts napkin while Huyen teases; restore late ballroom before looking toward Hoang and the goodbye menu. |

The shopping location now uses `bg_tam_c02_boutique_evening` rather than the
company lobby. Its display matches the premium gown and office clothing rails;
the CG does not confirm any purchase before the player's decision.

## Validation

Use isolated saves, never a player's save directory:

```powershell
& D:/RenPy/renpy-8.3.2-sdk/lib/py3-windows-x86_64/python.exe `
  D:/RenPy/renpy-8.3.2-sdk/renpy.py . `
  --savedir D:/Projects/RenPy_Games/LikeWindLikeCloud/tests/chapter_assets_saves `
  test chapter_two_assets --report-detailed --overwrite-screenshots
```

The suite covers premium, office, skipped shopping, unaffordable premium falling
back to office, and insufficient money for either outfit (including an office
retry). It exercises the dress-triggered approach plus all four Hoang introduction
choices and all three goodbye choices. Captures use 1080p and 720p.
Local captures are ignored under `tests/screenshots/chapter_two_assets/`.

Verified with Ren'Py 8.5.4.26101301+nightly on Windows: all five playthroughs
passed, 74/74 assertions, 34 CG captures at 1080p/720p. All generated source
images were inspected; representative in-game frames, including all three
late-party outfits and the reframed document/model actions, were inspected.
Final lint adds no warnings; existing Tam C07 and Yuuka C08 warnings remain.

No dialogue, translations, menu choices, money rules, scores or story flags are
changed by the asset integration. Added outfit conditionals select images only.
