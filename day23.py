import re

bots = [tuple(map(int, re.findall('-?\d+', x.strip()))) for x in open('data.in').readlines()]
one = sorted(bots, key=lambda x: x[3], reverse=True)[0]
print(len(list(filter(lambda x: sum([abs(x[0] - one[0]), abs(x[1] - one[1]), abs(x[2] - one[2])]) <= one[3], bots))))
