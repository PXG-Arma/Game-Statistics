#! /usr/bin/env python

#
# Common utility functions.
#
# Version: 0.2.0
# Date: 2023-07-17
#

# Stdlib imports
import sys

def eprint(*args, **kwargs):
    """Prints to the standard error output."""
    print(*args, file=sys.stderr, **kwargs) 
