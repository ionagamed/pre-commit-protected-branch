from __future__ import print_function

import os
import sys
import argparse

from pre_commit_protected_branch.util import CalledProcessError
from pre_commit_protected_branch.util import cmd_output


def is_on_branch(protected):
    try:
        branch = cmd_output('git', 'symbolic-ref', 'HEAD')
    except CalledProcessError:
        return False
    chunks = branch.strip().split('/')
    return '/'.join(chunks[2:]) in protected


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-b', '--branch', action='append',
        help='branch to disallow commits to, may be specified multiple times',
    )
    args = parser.parse_args(argv)

    protected = set(args.branch or ('master',))
    if is_on_branch(protected):
        if os.isatty(sys.stdout.fileno()):
            choice = input('You are trying to push into a protected branch (one of {}). Would you really like to do it [y/n]?')
            if choice == 'y':
                return 0
        else:
            print('Not in a tty, disallowing push')
            return 1
    return 0


if __name__ == '__main__':
    exit(main())
