#! /bin/bash
set -exo pipefail

TAG=$1

parse-changelog CHANGELOG.md $TAG
git tag -a $TAG -F <(parse-changelog CHANGELOG.md $TAG)
gh release create $TAG -t $TAG --notes-from-tag
