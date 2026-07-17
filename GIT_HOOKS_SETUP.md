# Git hook setup

This repository keeps its Git hooks in `.githooks/`.

To enable the version-bump pre-commit hook in a fresh clone, run:

```bash
./tools/setup_git_hooks.sh
```

What the script does:

- verifies that `.githooks/pre-commit` exists
- makes sure the hook is executable
- sets the local repository config `core.hooksPath` to `.githooks`
- verifies the config after writing it

You only need to run it once per clone.

To confirm the setup manually:

```bash
git config --get core.hooksPath
```

Expected output:

```text
.githooks
```

After that, normal commits will run `.githooks/pre-commit`, which updates `define config.version` in `game/options.rpy` based on the staged change size.
