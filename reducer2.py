import sys

s = 0.01

total = int(sys.argv[1])
min_support = total * s

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

#last
if current_pair and current_sum >= min_support:
    print(f"{current_pair[0]}\t{current_pair[1]}\t{current_sum}")