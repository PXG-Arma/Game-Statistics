#! /usr/bin/env python 

#
# filter-ops-zeus-missions.py
# Version: 0.1.0
# Date: 2023-07-17
#
# Filters the number of missions per Zeus from an ops statistics file.
#

# Local imports
import include.flow as flow

#
# Main
#

ops = flow.get_ops_or_die()

zeus_counts = {}

for op in ops:
    if len(op.zeus) > 0:
        count = zeus_counts.get(op.zeus, 0)
        zeus_counts[op.zeus] = count + 1

zeuses = list(zeus_counts.keys())
# Sort alphabetically
zeuses.sort()
# Sort by number of ops
zeuses.sort(key=zeus_counts.get, reverse=True)

# Output results

for zeus in zeuses:
    qzeus = '\"' + zeus + '\"'
    print(f"{qzeus:20} {zeus_counts[zeus]:2d}")
