from itertools import cycle

# with open("data.in", "r") as f:
#     content = f.readlines()
#     sums = [0]
#     s = 0
#     found = False
#     while not found:
#         for x in content:
#             x = int(x.strip())
#             s += x
#             if s in sums:
#                 found = True
#                 print(s)
#                 break
#
#             sums.append(s)
# print(list(sums) == set(sums))

# Matei
v, s, sums = list(map(int, open('data.in', 'r').readlines())), 0, set()
for x in cycle(v):
    s += x
    if s in sums:
        print(s)
        break
    sums.add(s)
