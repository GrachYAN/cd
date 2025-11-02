import sys

candidates = set()
with open('candidate_pairs.txt', 'r') as f:
    for line in f:
        x, y = line.strip().split('\t')
        candidates.add((x, y))

for line in sys.stdin:
    basket = set(line.strip().split())
    for a, b in candidates:
        if a in basket and b in basket:
            print(f"{a}\t{b}\t1")
