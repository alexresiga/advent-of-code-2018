DEPTH = 510
TARGET = (10, 10)
ROWS, COLS = TARGET[1] + 7, TARGET[0] + 7
region = {0: '.', 1: '=', 2: '|'}
risk = {'.': 0, '=': 1, '|': 2}
maze = [['.' for _ in range(COLS)] for _ in range(ROWS)]
index = [[0 for _ in range(COLS)] for _ in range(ROWS)]
for i in range(COLS):
    for j in range(ROWS):
        if i == 0 and j == 0:
            index[j][i] = (0 + DEPTH) % 20183
        elif (i, j) == TARGET:
            index[j][i] = (0 + DEPTH) % 20183
        elif i == 0:
            index[j][i] = (j * 48271 + DEPTH) % 20183
        elif j == 0:
            index[j][i] = (i * 16807 + DEPTH) % 20183
        else:
            index[j][i] = (DEPTH + index[j - 1][i] * index[j][i - 1]) % 20183
for line in index:
    print(line)

for i in range(COLS):
    for j in range(ROWS):
        maze[j][i] = region[index[j][i] % 3]
for line in maze:
    print(line)
print(sum(risk[maze[j][i]] for i in range(TARGET[0]+1) for j in range(TARGET[1]+1)))
