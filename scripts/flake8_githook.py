#!/usr/bin/env python

# To use the Git hook on any commit, add a pre-commit file in the
# .git/hooks directory containing this scropt
# Source:
# https://flake8.readthedocs.org/en/2.0/vcs.html

import sys
from flake8.run import git_hook

COMPLEXITY = 10
STRICT = False

if __name__ == '__main__':
    sys.exit(git_hook(complexity=COMPLEXITY, strict=STRICT, ignore='E501'))
