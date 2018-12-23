lines = [x.strip() for x in open('data.in').readlines()]
positions = [x.replace("position=", '').replace('velocity=', '').replace('<', '').replace('>', '').replace(',', '') for
             x
             in lines]
elems = [[int(y) for y in x.split(' ') if y != ''] for x in positions]

for s in range(12345, 12346):

    points = set((x[1] + s * x[3], x[0] + s * x[2]) for x in elems)
    north, south = min(x[1] for x in points), max([x[1] for x in points])
    west, east = min(x[0] for x in points), max([x[0] for x in points])
    if east - abs(west) <= 170:
        print(s)
        for i in range(west, east + 1):
            for j in range(north, south + 1):
                print('#', end=' ') if (i, j) in points else print('.', end=' ')
            print()
        print()
