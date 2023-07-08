#! /usr/bin/env python3

#
# Common utility functions.
#

import sys

def eprint(*args, **kwargs):
    """Prints to the standard error output."""
    print(*args, file=sys.stderr, **kwargs) 
