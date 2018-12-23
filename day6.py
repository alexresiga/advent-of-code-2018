def manhattan_distance(ans, b):
    return abs(ans[0] - b[0]) + abs(ans[1] - b[1])


with open('data.in', 'r') as f:
    points = [(int((x.split(", ")[1])), int(x.split(", ")[0])) for x in [x.strip() for x in f.readlines()]]
    label = {p: i for i, p in enumerate(points, 1)}
    distances = {(i, j): 500 for i in range(400) for j in range(400)}
    dist = {(i, j): 0 for i in range(400) for j in range(400)}
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    finite = {label[p]: True for p in points}
    grid = [[0 for i in range(400)] for j in range(400)]
    for i in range(400):
        for j in range(400):
            for p in points:
                dist[(i, j)] += manhattan_distance((i, j), p)
                if manhattan_distance((i, j), p) == distances[(i, j)]:
                    grid[i][j] = 0
                if manhattan_distance((i, j), p) < distances[(i, j)]:
                    distances[(i, j)] = manhattan_distance((i, j), p)
                    grid[i][j] = label[(p[0], p[1])]
    for i in range(400):
        for j in range(400):
            for d in directions:
                if i + d[0] < 0 or i + d[0] > 399 or j + d[0] < 0 or j + d[0] > 399:
                    if grid[i][j] != 0:
                        finite[grid[i][j]] = False
    area = {p: 0 for p in {k: v for k, v in finite.items() if v}.keys()}
    for label in {k: v for k, v in finite.items() if v}.keys():
        for i in range(400):
            for j in range(400):
                if grid[i][j] == label:
                    area[label] += 1
    print(sorted(area.items(), key=lambda x: x[1], reverse=True))
    print({k: v for k, v in dist.items() if v < 10000}.items().__len__())
