#! /usr/bin/env python3 

#
# filter-ops-map-freq.py
# Version: 0.2.0
# Date: 2023-07-08
#
# Filters map usage data from an ops statistics file.
#
# Outputs two space-separated columns: map name (quoted) and number of times
# a map was used in ops. Data is sorted by op count and alphabetically by
# map name. The result is written to the standard output.
#
# Usage:
# python filter-ops-map-freq.py OPS_DATA_FILE
#

#
# Imports
#

# Stdlib imports
import sys

# Local imports
import include.ops as ops
from include.util import eprint

#
# Main
#

# Parse data file

if len(sys.argv) < 2:
    eprint('Missing data file name.')
    sys.exit(1)

path = sys.argv[1]
ops = ops.parse_ops(path)

if ops is None:
    eprint('Failed to parse op data.')
    sys.exit(1)

# DEBUG
#from pprint import pprint
#for op in ops:
#    pprint(vars(op))

# Process data

map_counts = {}

for op in ops:
    if len(op.map) > 0:
        count = map_counts.get(op.map, 0)
        map_counts[op.map] = count + 1

maps = list(map_counts.keys())
# Sort alphabetically
maps.sort()
# Sort by number of ops
maps.sort(key=map_counts.get, reverse=True)

# DEBUG
#from pprint import pprint
#pprint(map_counts)
#pprint(maps)

# Output results

for map in maps:
    qmap = '\"' + map + '\"'
    print(f"{qmap:20} {map_counts[map]:2d}")
