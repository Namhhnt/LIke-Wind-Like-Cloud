#!/usr/bin/env sh

set -eu

repo_root=$(git rev-parse --show-toplevel)

hooks_dir="$repo_root/.githooks"
pre_commit_hook="$hooks_dir/pre-commit"

if [ ! -d "$hooks_dir" ]; then
    printf 'Error: hooks directory not found: %s\n' "$hooks_dir" >&2
    exit 1
fi

if [ ! -f "$pre_commit_hook" ]; then
    printf 'Error: pre-commit hook not found: %s\n' "$pre_commit_hook" >&2
    exit 1
fi

chmod +x "$pre_commit_hook"

git config core.hooksPath .githooks

configured_path=$(git config --get core.hooksPath)

if [ "$configured_path" != ".githooks" ]; then
    printf 'Error: expected core.hooksPath to be .githooks, got %s\n' "$configured_path" >&2
    exit 1
fi

printf 'Git hooks configured successfully.\n'
printf 'core.hooksPath=%s\n' "$configured_path"
printf 'Active hook: %s\n' "$pre_commit_hook"
