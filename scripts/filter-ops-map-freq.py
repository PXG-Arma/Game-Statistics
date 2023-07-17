#! /usr/bin/env python 

#
# filter-ops-map-freq.py
# Version: 0.3.0
# Date: 2023-07-17
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
import include.flow as flow

#
# Main
#

# Parse data file

ops = flow.get_ops_or_die()

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
