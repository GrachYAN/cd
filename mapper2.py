#!/usr/bin/env python3
import sys

# 加载候选对（假定通过分布式缓存传入）
candidates = set()
with open('candidate_pairs.txt', 'r') as f:
    for line in f:
        x, y = line.strip().split('\t')
        candidates.add((x, y))

# 统计候选对出现次数
for line in sys.stdin:
    basket = set(line.strip().split())
    for a, b in candidates:
        if a in basket and b in basket:
            print(f"{a}\t{b}\t1")
