"""Validate chapter-four art inventory and prove story logic is unchanged.

Run with Pillow installed: python tools/validate_chapter_four_assets.py
"""
import json
import re
import subprocess
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "60c06cb"


def narrative(text):
    return [
        line for line in text.splitlines()
        if line.strip() and not re.match(r"\s*(#|scene |with )", line)
    ]


def main():
    manifest = json.loads((ROOT / "Specs/tam_c04_asset_manifest.json").read_text(encoding="utf-8"))
    prompts = json.loads((ROOT / "Specs/tam_c04_asset_prompts.json").read_text(encoding="utf-8"))
    assets = manifest["assets"]
    assert len(assets) == 45
    assert len({a["id"] for a in assets}) == 45
    assert {a["id"] for a in assets} == {p["id"] for p in prompts}
    total = 0
    for asset in assets:
        path = ROOT / asset["output"]
        with Image.open(path) as image:
            image.load()
            assert image.size == (1920, 1080), path
            assert image.mode == "RGB", path
        total += path.stat().st_size
    for prompt in prompts:
        assert prompt["prompt"]
        for reference in prompt["references"]:
            assert (ROOT / reference).is_file(), reference

    declarations = (ROOT / "game/scripts/cgs_tam_c04.rpy").read_text(encoding="utf-8")
    declared = dict(re.findall(r'^image (\w+) = "([^"]+)"', declarations, re.M))
    assert len(declared) == 44
    for path in declared.values():
        assert (ROOT / "game" / path).is_file(), path
    directory = ROOT / "game/story/tam/tam_c04_between_work_and_hearts"
    used = set()
    for path in directory.glob("*.rpy"):
        source = path.read_text(encoding="utf-8")
        old = subprocess.check_output(
            ["git", "show", f"{BASELINE}:{path.relative_to(ROOT).as_posix()}"], cwd=ROOT
        ).decode("utf-8")
        assert narrative(source) == narrative(old), f"Narrative or logic changed: {path}"
        used.update(re.findall(r"scene (cg_tam_c04_\w+)", source))
        for name in re.findall(r"scene ((?:cg_tam_c04_|bg_c04_)\w+)", source):
            assert name in declared, name
        # Every static CG beat must be cleared by a background before any menu,
        # return, code, or another narrative line can change its meaning.
        for match in re.finditer(r"(?m)^(\s*)scene (cg_tam_c04_\w+)\n", source):
            tail = source[match.end():].splitlines()
            assert tail[0].strip() == "with dissolve"
            assert tail[2].strip().startswith("scene bg_"), (path, match[2])
    assert used == {name for name in declared if name.startswith("cg_")}
    print(f"PASS: {len(assets)} images; 44 declarations; {len(used)} CGs used; "
          f"141 source files preserve narrative/logic; {total / 1048576:.2f} MiB")


if __name__ == "__main__":
    main()
