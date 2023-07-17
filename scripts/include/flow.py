#! /usr/bin/env python

#
# Common program flow functions.
#
# Version: 0.1.0
# Date: 2023-07-17
#

# Stdlib imports
import sys

# Local imports
from include.ops import parse_ops
from include.util import eprint

def get_ops_or_die():
    """Reads command line parameters and parses the given op data file.
    Returns an Op object. Prints to STDERR and exits in any case of failure.
    """
    if len(sys.argv) < 2:
        eprint('Missing data file name.')
        sys.exit(1)

    path = sys.argv[1]
    ops = parse_ops(path)

    if ops is None:
        eprint('Failed to parse op data.')
        sys.exit(1)

    return ops
