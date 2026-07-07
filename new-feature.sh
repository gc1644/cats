#!/usr/bin/env bash

set -e

if [ $# -eq 0 ]; then
	echo "Usage: ./new-feature.sh \"Commit  message\""
	exit 1
fi

MESSAGE="$1"

BRANCH=$(echo "$MESSAGE" \
	| tr '[:upper:]' '[:lower:]' \
	| sed 's/ /-/g')

echo "Creating branch: $BRANCH"

CURRENT_BRANCH=$(git branch --show-current)

if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "Please switch to 'main' before running this script."
    exit 1
fi

CURRENT_BRANCH=$(git branch --show-current)

if [ "$CURRENT_BRANCH" != "main" ]; then
    if ! git diff --quiet || ! git diff --cached --quiet; then
        echo "You have uncommitted changes on branch '$CURRENT_BRANCH'."
        echo "Please commit them or stash them before switching to main."
        exit 1
    fi

    git checkout main
fi

git pull --ff-only

git checkout -b "$BRANCH"

git add .

if git diff --cached --quiet; then
    echo "Nothing to commit."
    exit 0
fi

git commit -m "$MESSAGE"

git push -u origin "$BRANCH"

git checkout main

echo
echo "done!"
echo
echo "✅ Branch '$BRANCH' pushed successfully!"
echo "Open GitHub and create a Pull Request."
