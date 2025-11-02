import sys

candidate_set = set()

for line in sys.stdin:
    a, b = line.strip().split('\t')
    candidate_set.add((a, b))

for a, b in candidate_set:
    print(f"{a}\t{b}")
