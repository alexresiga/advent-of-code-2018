def adjacent(x, y, point):
    fill = {'.': '|', '|': '#'}
    cnt, l, tree = 0, False, False
    dirs = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]
    for d in dirs:
        if 0 <= x + d[0] <= 49 and 0 <= y + d[1] <= 49:
            if point in fill.keys():
                if area[x + d[0]][y + d[1]] == fill[point]:
                    cnt += 1
            else:
                if area[x + d[0]][y + d[1]] == '#':
                    l = True
                elif area[x + d[0]][y + d[1]] == '|':
                    tree = True
    if point in fill.keys() and cnt >= 3:
        grid[x][y] = fill[point]
    elif point in fill.keys() and cnt < 3:
        grid[x][y] = point
    else:
        if l and tree:
            grid[x][y] = '#'
        else:
            grid[x][y] = '.'


area = [list(x.strip()) for x in open('data.in').readlines()]
grid = [[None for _ in range(50)] for _ in range(50)]
s = []
for g in range(1, 1001):
    grid = [[None for _ in range(50)] for _ in range(50)]
    for i in range(len(area)):
        for j in range(len(area[i])):
            adjacent(i, j, area[i][j])
    area[:] = grid
    snapshot = '\n'.join(''.join(line) for line in area)
    if snapshot in s:
        i = s.index(snapshot)
        period = g - (1 + i)
        while (i + 1) % period != 1000000000 % period:
            i += 1
        print(s[i].count('|') * s[i].count('#'))
        break
    else:
        s.append(snapshot)
