#!/usr/bin/env python3
import sys
from collections import Counter
from itertools import combinations

# 支持度比例
s = 0.01

# 读取所有篮子
basket_data = [line.strip().split() for line in sys.stdin if line.strip()]
basket_total = len(basket_data)
local_support = int(basket_total * s)

# 统计单品
item_counter = Counter()
for basket in basket_data:
    item_counter.update(basket)

# 筛选局部频繁单品
freq_items = set([item for item, cnt in item_counter.items() if cnt >= local_support])

# 统计频繁对
pair_counter = Counter()
for basket in basket_data:
    # 只考虑频繁单品
    valid_items = [item for item in basket if item in freq_items]
    # 生成所有两两组合
    for pair in combinations(sorted(valid_items), 2):
        pair_counter[pair] += 1

# 输出局部频繁对作为候选
for pair, cnt in pair_counter.items():
    if cnt >= local_support:
        print(f"{pair[0]}\t{pair[1]}")
