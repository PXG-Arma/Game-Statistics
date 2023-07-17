#! /usr/bin/env python

#
# Common functionality for parsing op data.
#
# Version: 0.1.0
# Date: 2023-07-17
#

#
# Imports
#

from include.util import eprint

#
# Classes
#

class Op:
    """Statistics data for a single op."""

    """Integer ID of the op. Increments from 1."""
    id = -1
    """Date of the op as string in format YYYY-MM-DD."""
    date = ''
    """Op name string."""
    name = ''
    """Op type string."""
    type = ''
    """Name of the Zeus of the op."""
    zeus = ''
    """Number of players joined (excluding Zeus)."""
    n_players = -1
    """Number of players signed up before the op."""
    n_signed_up = -1
    """Respawn system string."""
    respawn = ''
    """Mine threat string."""
    mine_threat = 'No'
    """Artillery threat string."""
    artillery_threat = 'No'
    """Player faction name."""
    faction = ''

#
# Functions
#

def parse_ops(path):
    """Parses op statistics data from the file with given path.
    Returns a list of Op objects on success, or None on failure.
    """
    data = []
    line_number = 0

    try:
        with open(path) as file:
            for line in file:
                line_number += 1

                if len(line.strip()) == 0:
                    continue

                if 1 == line_number:
                    pass
                else:
                    res = _parse_op_line(line)
                    if res is None:
                        eprint(f"Invalid data at line {line_number}.")
                    else:
                        data.append(res)
    except Exception as e:
        eprint(f"Failed to read file '{path}':\n{e}")
        return None

    return data

def _parse_op_line(line):
    """Parses a line with op statistics data.
    Returns an Op object, or None on error.
    """
    words = line.split('\t')
    words = [w.strip() for w in words]

    # Begin: column config
    # Required number of columns
    REQ_COLUMNS = 12
    if len(words) < REQ_COLUMNS:
        return None

    op = Op()
    # Column associations and data types
    op.id = int(words[0])
    op.date = words[1]
    op.name = words[2]
    op.map = words[3]
    op.type = words[4]
    op.zeus = words[5]
    op.n_players = int(words[6])
    op.n_signed_up = int(words[7])
    op.respawn = words[8]
    op.mine_threat = words[9]
    op.artillery_threat = words[10]
    op.faction = words[11]
    # End: column config

    return op
