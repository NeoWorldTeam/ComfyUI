#!/bin/bash

echo "Fetching updates for main repository..."
git fetch --all

echo "Resetting any conflicted files to remote version..."
git diff --name-only --diff-filter=U | while read -r file; do
    git checkout --theirs "$file"
    git add "$file"
done

echo "Updating main repository..."
git pull --rebase

echo "Updating submodules..."
git submodule foreach --recursive 'git fetch --all'
git submodule foreach --recursive 'git merge --no-commit --no-ff -s recursive -X theirs'

echo "Update complete."
