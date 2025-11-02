#!/usr/bin/env python3
import sys

# 存储所有候选对
candidates = set()
for line in sys.stdin:
    a, b = line.strip().split('\t')
    candidates.add((a, b))

# 输出去重后的候选对
for a, b in sorted(candidates):
    print(f"{a}\t{b}")
