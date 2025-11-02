#!/usr/bin/env python3
import sys

candidate_set = set()
for line in sys.stdin:
    items = line.strip().split('\t')
    if len(items) == 2:
        candidate_set.add(tuple(items))

for pair in candidate_set:
    print(f"{pair[0]}\t{pair[1]}")
