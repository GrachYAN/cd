#!/usr/bin/env python3
import sys

SUPPORT_RATIO = 0.01

# 1. 读取总篮子数
num_basket = int(sys.argv[1])
global_support = int(num_basket * SUPPORT_RATIO)

# 2. 累加pair计数
last_pair = None
last_count = 0

for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) != 3:
        continue
    pair = (parts[0], parts[1])
    count = int(parts[2])
    if pair == last_pair:
        last_count += count
    else:
        if last_pair and last_count >= global_support:
            print(f"{last_pair[0]}\t{last_pair[1]}\t{last_count}")
        last_pair = pair
        last_count = count

# 3. 输出最后一个pair
if last_pair and last_count >= global_support:
    print(f"{last_pair[0]}\t{last_pair[1]}\t{last_count}")
