from collections import Counter
from itertools import combinations


def get_input():
    return map(str, open("day2.txt"))


ch2 = 0
ch3 = 0
for id in get_input():
    chars_counts = list(Counter(id).values())
    if 2 in chars_counts: ch2 += 1
    if 3 in chars_counts: ch3 += 1
print(ch2 * ch3)


def str_diff(a, b):
    return len([x for x, y in zip(a, b) if x != y])


closest_ids = min([(str_diff(id1, id2), id1, id2) for id1, id2 in list(combinations(get_input(), 2))])
print(''.join([x for x, y in zip(closest_ids[1], closest_ids[2]) if x == y]))
