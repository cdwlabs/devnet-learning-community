#! /usr/bin/env sh

#### Use markdownlint (mdl) To Lint Markdown Files
# A container image exists for Ruby, that can be used to easily install the
# markdownlint (mdl) tool. A style file exists in this directory to handle the
# line break functionality by leaving 2 spaces at the end of the line.
#
# We look for an exit code of 0 ($? in BASH) to signal success. Any non-zero
# value indicates failure.
#
# How To Use
#   podman run --rm -it -v .:/app ruby:2.6-alpine sh
#   gem install mdl
#   cd /app
#   sh tests/linting.markdown.sh
#
# References:
#   Upstream Markdown Spec:
#     http://daringfireball.net/projects/markdown/syntax
#   The markdownlint tool:
#     https://github.com/markdownlint/markdownlint
#   Creating and Using MDL Styles: 
#     https://github.com/markdownlint/markdownlint/blob/master/docs/creating_styles.md
#   Reason For The Style File With br_spaces Usage
#     https://github.com/markdownlint/markdownlint/commit/7f322b33d24262a0dfa69133bc428c379b82ca18

EXIT=0

IFS=$'\n'
for MARKDOWN in `find . -name "*.md" | sort`
do
  mdl "$MARKDOWN" -s tests/linting.markdown.mdlstyle.rb
  RESULT="$?"
  if [ $RESULT -ne "0" ]
  then
    EXIT="$RESULT"
  fi
done
unset IFS

exit $EXIT
