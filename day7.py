# with open('data.in', 'r') as f:
#     pairs = [(x.split(" ")[1], x.split(" ")[-3]) for x in [x.strip() for x in f.readlines()]]
#     steps = set(x[0] for x in pairs).union(set(x[1] for x in pairs))
#     stack = [sorted(list(steps.difference(set(x[1] for x in pairs))))[0]]
#     ready = sorted(list(steps.difference(set(x[1] for x in pairs))))[1:]
#     while len(pairs):
#         for s in stack:
#             for p in pairs:
#                 if p[0] == s:
#                     tail = [n for n in pairs if n[1] == p[1] and n[0] != s]
#                     pre = [a for a in tail if a[0] not in stack]
#                     if p[1] not in ready and not pre:
#                         ready.append(p[1])
#                     pairs = [x for x in pairs if x != p]
#             try:
#                 ready.sort()
#                 stack.append(ready[0])
#                 ready.remove(ready[0])
#             except IndexError:
#                 pass
#     print(''.join(stack))
# PART 2
from collections import defaultdict


def add_task(xx):
    work_queue.append(xx)


def start_work():
    global work_queue
    while len(events) < 5 and work_queue:
        x = min(work_queue)
        work_queue = [y for y in work_queue if y != x]
        events.append((t + 61 + ord(x) - ord('A'), x))


E = defaultdict(list)
D = defaultdict(int)
for line in open('data.in'):
    words = line.split()
    x, y = words[1], words[7]
    E[x].append(y)
    D[y] += 1

for k in E:
    E[k] = sorted(E[k])

t = 0
events = []
work_queue = []

for k in E:
    if not D[k]:
        add_task(k)
start_work()
while events or work_queue:
    t, x = min(events)
    print(t, x)
    events = [y for y in events if y != (t, x)]
    for y in E[x]:
        D[y] -= 1
        if not D[y]:
            add_task(y)
    start_work()
print(t)
