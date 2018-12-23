def next_gen(cur, s):
    start = min(cur)
    end = max(cur)
    x = set()
    for i in range(start - 3, end + 4):
        pattern = ''.join('#' if i + k in cur else '.' for k in [-2, -1, 0, 1, 2])
        if pattern in s:
            x.add(i)
    return x


content = [x.strip() for x in open('data.in').readlines() if x]
initial_state = content[0].split(' ')[2]
spread = set(x[:5] for x in content[1:] if x[-1] == '#')
print(spread)

current = set(i for i, c in enumerate(initial_state) if c == '#')
for _ in range(20):
    current = next_gen(current, spread)
print(sum(current))

# PART 2
# ls = 0
# for i in range(2000):
#     current = next_gen(current, spread)
#     s = sum(current)
#     print(i, s, s - ls)
#     ls = s
# print((50000000000 - 2000) * 80 + sum(current))
