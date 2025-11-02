#!/usr/bin/env python3
import sys

# 支持度比例
SUPPORT_RATIO = 0.01

# 统计总篮子数（假定通过命令行参数传入）
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--num_baskets', type=int, required=True)
args = parser.parse_args()
total_baskets = args.num_baskets
min_support = int(total_baskets * SUPPORT_RATIO)

# 累加计数
current_pair = None
current_sum = 0

for line in sys.stdin:
    a, b, cnt = line.strip().split('\t')
    pair = (a, b)
    cnt = int(cnt)
    if pair == current_pair:
        current_sum += cnt
    else:
        if current_pair and current_sum >= min_support:
            print(f"{current_pair[0]}\t{current_pair[1]}\t{current_sum}")
        current_pair = pair
        current_sum = cnt

# 最后一个pair
if current_pair and current_sum >= min_support:
    print(f"{current_pair[0]}\t{current_pair[1]}\t{current_sum}")
