# TRANSLATION DOMAIN

## OVERVIEW
`game/tl/` mirrors source script filenames by locale. Treat it as a synchronization layer, not an independent feature area.

## STRUCTURE
```text
game/tl/
├── None/common.rpym      # Baseline/common translation data.
└── vietnamese/
    ├── script.rpy
    ├── screens.rpy
    └── options.rpy
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| Story line translations | `vietnamese/script.rpy` | Mirrors `game/script.rpy`. |
| UI/menu string translations | `vietnamese/screens.rpy` | Mirrors `game/screens.rpy`; currently has a duplicate-string failure. |
| Title/config translations | `vietnamese/options.rpy` | Mirrors `game/options.rpy`. |
| Common/base string reference | `None/common.rpym` | Useful reference; not where custom locale work should start. |

## CONVENTIONS
- Keep locale files aligned with source filenames and responsibilities.
- When source UI text changes, update the mirrored locale file in the same pass.
- One locale should have one `old`/`new` pair per source string.
- Preserve file locality: screen text stays in `screens.rpy`, story lines in `script.rpy`.

## ANTI-PATTERNS
- Do not duplicate the same `old` string inside one locale file.
- Do not hand-edit compiled translation artifacts such as `.rpymc`.
- Do not move translations into unrelated files just to make collisions disappear.
- Do not assume `None/common.rpym` is the place for Vietnamese customization.

## NOTES
- Current known failure from `traceback.txt`: `game/tl/vietnamese/screens.rpy` defines `old "Rolls forward to later dialogue."` more than once.
- Translation maintenance here is filename-mirrored, not centralized in one master locale file.
