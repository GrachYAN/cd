#!/usr/bin/env python3
import sys

# 加载候选对
candidate_pairs = set()
with open("candidate_pairs.txt") as f:
    for line in f:
        items = line.strip().split('\t')
        if len(items) == 2:
            candidate_pairs.add(tuple(items))

for line in sys.stdin:
    basket = set(line.strip().split())
    for pair in candidate_pairs:
        if pair[0] in basket and pair[1] in basket:
            print(f"{pair[0]}\t{pair[1]}\t1")
