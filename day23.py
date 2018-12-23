import re


def manhattan_distance(a: tuple, b: tuple):
    return sum([abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2])])


bots = [tuple(map(int, re.findall('-?\d+', x.strip()))) for x in open('data.in').readlines()]
one = sorted(bots, key=lambda x: x[3], reverse=True)[0]
print(sum(1 for bot in bots if manhattan_distance(one, bot) <= one[3]))
