import sys
from collections import Counter
from itertools import combinations

s = 0.01

baskets = [line.strip().split() for line in sys.stdin if line.strip()]
total = len(baskets)
local_support = int(total * s)

# item
item_counter = Counter()
for basket in baskets:
    item_counter.update(basket)

freq_items = set([item for item, cnt in item_counter.items() if cnt >= local_support])

# pair
pair_counter = Counter()
for basket in baskets:
    valid_items = [item for item in basket if item in freq_items]
    for pair in combinations(sorted(valid_items), 2):
        pair_counter[pair] += 1

for pair, cnt in pair_counter.items():
    if cnt >= local_support:
        print(f"{pair[0]}\t{pair[1]}")
