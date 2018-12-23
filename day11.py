from math import inf
from itertools import product

GSN = 8772
grid = [[0 for i in range(300)] for j in range(300)]
for i, j in product(range(300), repeat=2):
    grid[i][j] = (((j + 11) * (i + 1) + GSN) * (j + 11) // 100 % 10) - 5

s = [[0] * 300 for _ in range(301)]
for r, c in product(range(1, 301), range(300)):
    s[r][c] = s[r - 1][c] + grid[r - 1][c]

max_sum = -inf
max_row_start = -1
max_col_start = -1
max_row_end = -1
max_col_end = -1
max_size = -1
for r1 in range(1, 301):
    for r2 in range(r1, 301):
        s1 = [0 for _ in range(300)]
        for c in range(300):
            s1[c] = s[r2][c] - s[r1 - 1][c]
        maxim = 0
        c1 = 0
        for c in range(300):
            maxim = s1[c] + maxim
            if maxim <= 0:
                maxim = 0
                c1 = c + 1
            if maxim > max_sum and r2 - r1 == c - c1:
                max_sum = maxim
                max_row_start = r1 - 1
                max_col_start = c1
                max_row_end = r2 - 1
                max_col_end = c
                max_size = c - c1

print(max_row_start, max_col_start)
print(max_size)
