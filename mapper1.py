#!/usr/bin/env python3
import sys
from collections import defaultdict
from itertools import combinations

SUPPORT_RATIO = 0.01

# 1. 收集所有篮子
baskets = []
for line in sys.stdin:
    basket = line.strip().split()
    if basket:
        baskets.append(basket)

# 2. 计算本地支持度阈值
local_support = int(len(baskets) * SUPPORT_RATIO)

# 3. 统计频繁单品
item_count = defaultdict(int)
for basket in baskets:
    for item in basket:
        item_count[item] += 1
freq_items = set([item for item, cnt in item_count.items() if cnt >= local_support])

# 4. 统计频繁对
pair_count = defaultdict(int)
for basket in baskets:
    valid_items = [item for item in basket if item in freq_items]
    for pair in combinations(sorted(valid_items), 2):
        pair_count[pair] += 1

# 5. 输出频繁对候选
for pair, cnt in pair_count.items():
    if cnt >= local_support:
        print(f"{pair[0]}\t{pair[1]}")
