from string import ascii_lowercase


def has_enough(id, times):
    return [x for x in ascii_lowercase if id.count(x) == times]


# with open("data.in", "r") as f:
#     content = [x.strip() for x in f.readlines()]
#     twos, threes = 0, 0
#     for e in content:
#         if has_enough(e, 2):
#             twos += 1
#         if has_enough(e, 3):
#             threes += 1
#     print(threes*twos)

# PART 2
def good_boxes(a, b):
    return [a[n] for n in range(len(a)) if a[i] == b[i]]


with open("data.in", 'r') as f:
    content = [x.strip() for x in f.readlines()]
    for i in content[:-1]:
        for j in content[content.index(i):]:
            if len(good_boxes(i, j)) == len(i) - 1:
                print(''.join(good_boxes(i, j)))
