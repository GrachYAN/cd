#!/usr/bin/env python3
import sys

# 合并所有候选对
candidate_set = set()

for line in sys.stdin:
    a, b = line.strip().split('\t')
    candidate_set.add((a, b))

# 输出去重后的候选对
for a, b in candidate_set:
    print(f"{a}\t{b}")
