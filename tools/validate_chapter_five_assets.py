"""Check C05 images, declarations, bounded CG cues and unchanged narrative."""
import json
import re
import subprocess
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / 'game/story/tam/tam_c05_sunday_date'


def narrative(text):
    return [line for line in text.splitlines()
            if line.strip() and not re.match(r'\s*(#|scene |with )', line)]


def main():
    manifest = json.loads((ROOT / 'Specs/tam_c05_asset_manifest.json').read_text(encoding='utf-8'))
    shots = json.loads((ROOT / 'Specs/tam_c05_asset_integration.json').read_text(encoding='utf-8'))
    assets = manifest['assets']
    prompts = json.loads((ROOT / 'Specs/tam_c05_asset_prompts.json').read_text(encoding='utf-8'))['assets']
    assert len(prompts) == len(assets)
    assert {p['id'] for p in prompts} == {a['id'] for a in assets}
    assert all(p['prompt'] for p in prompts)
    assert len(assets) == 32
    assert len({a['id'] for a in assets}) == 32
    assert sum(a['type'] == 'cg' for a in assets) == 24
    total = 0
    for asset in assets:
        path = ROOT / asset['output']
        with Image.open(path) as image:
            image.load()
            assert image.size == (1920, 1080), path
            assert image.mode == 'RGB', path
        total += path.stat().st_size
        for reference in asset['references']:
            assert (ROOT / reference).is_file(), reference
    declarations = dict(re.findall(r'^image (\w+) = "([^"]+)"',
        (ROOT / 'game/scripts/cgs_tam_c05.rpy').read_text(encoding='utf-8'), re.M))
    assert set(declarations) == {a['id'] for a in assets}
    for path in declarations.values():
        assert (ROOT / 'game' / path).is_file(), path
    used = set()
    for path in DIRECTORY.glob('*.rpy'):
        source = path.read_text(encoding='utf-8-sig')
        old = subprocess.check_output(['git', 'show', manifest['baseline'] + ':' + path.relative_to(ROOT).as_posix()], cwd=ROOT).decode('utf-8-sig')
        assert narrative(source) == narrative(old), 'Narrative/logic changed: ' + str(path)
        used.update(re.findall(r'^\s*scene ((?:cg_tam_c05_|bg_c05_)\w+)', source, re.M))
        for shot in [s for s in shots if s['file'] == path.name]:
            cue = 'scene ' + shot['id'] + '\n'
            assert cue in source, shot
        # Every CG is bounded to one existing say line. It must be cleared before
        # later menus, flags, gifts or movements can contradict the still image.
        for match in re.finditer(r'(?m)^([ \t]*)scene (cg_tam_c05_\w+)\n', source):
            tail = source[match.end():].splitlines()
            assert tail[0].strip() == 'with dissolve'
            assert tail[1].lstrip().startswith('"'), (path, match[2])
            assert tail[2].strip().startswith('scene bg_'), (path, match[2])
    assert used == set(declarations), (set(declarations) - used)
    print(f'PASS: 32 images (24 CGs + 8 BGs); all declared and used; '
          f'5 source files preserve narrative/logic; {total / 1048576:.2f} MiB')


if __name__ == '__main__':
    main()
