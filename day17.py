from math import inf

grid = [['.' for _ in range(509)] for _ in range(16)]
grid[0][500] = '+'
content = [sorted(x.strip().split(', '), reverse=True) for x in open('data.in').readlines()]
max_y, min_y = -inf, inf
for line in content:

    line[0] = line[0].replace('y=', '')
    line[1] = line[1].replace('x=', '')
    if '..' not in line[0]:
        line[1]: str = line[1].split('..')
        if int(line[0]) > max_y:
            max_y = int(line[0])
        if int(line[0]) < min_y:
            min_y = int(line[0])
        for x in range(int(line[1][0]), int(line[1][1]) + 1):
            grid[int(line[0])][x] = '#'
    else:
        line[0] = line[0].split('..')

        if int(line[0][1]) > max_y:
            max_y = int(line[0][1])
        if int(line[0][0]) < min_y:
            min_y = int(line[0][0])
        for y in range(int(line[0][0]), int(line[0][1]) + 1):
            grid[y][int(line[1])] = '#'


def flow():
    xs, ys = 0, 500
    for _ in range(10):

        while grid[xs + 1][ys] not in '#~' and xs < max_y:
            print(xs)
            xs += 1
            grid[xs][ys] = '|'
        overflow = False
        of = -1
        left, right = ys, ys

        while grid[xs][right + 1] is not '#':
            right += 1
            if grid[xs + 1][right] not in '#~':
                overflow = True
                of = right
                break
        while grid[xs][left - 1] is not '#':
            left -= 1

            if grid[xs + 1][left] not in '#~':
                overflow = True
                of = left
                break
        if overflow:
            for a in range(min(of, right, left), max(of, right, left) + 1):
                grid[xs][a] = '|'
            ys = of
        else:
            left, right = ys, ys
            grid[xs][ys] = '~'
            while grid[xs][left - 1] not in '#~':
                left -= 1
                grid[xs][left] = '~'
            while grid[xs][right + 1] not in '#~':
                right += 1
                grid[xs][right] = '~'
            xs -= 1


flow()
for i in range(16):
    for j in range(494, 509):
        print(grid[i][j], end=' ')
    print()
