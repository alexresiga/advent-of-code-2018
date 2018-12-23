dirs = {'<': (0, -1), '>': (0, 1), 'v': (1, 0), '^': (-1, 0)}
positions = []
turn = {'^': ['<', '^', '>'], '>': ['^', '>', 'v'], '<': ['v', '<', '^'], 'v': ['>', 'v', '<']}
inter = {'>': '-', '<': '-', '^': chr(124), 'v': chr(124)}
content = [list(x.rstrip('\n')) for x in open('data.in', 'r').readlines()]

for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] in '<>v^':
            positions.append([content[i][j], i, j, 0, None])
mid = []
pos = set()
while len(positions) > 1:
    pos.add(len(positions))

    for p in positions:

        nextt: str = content[p[1] + dirs[p[0]][0]][p[2] + dirs[p[0]][1]]

        if nextt in ['-', chr(92), '/', chr(124)]:
            mid.append((nextt, p[1] + dirs[p[0]][0], p[2] + dirs[p[0]][1]))
            if p[4] == '+':
                content[p[1]][p[2]] = '+'
            elif p[4] in [chr(92), '/']:
                content[p[1]][p[2]] = p[4]
            else:
                content[p[1]][p[2]] = inter[p[0]]
            p[4] = nextt
            p[1] = p[1] + dirs[p[0]][0]
            p[2] = p[2] + dirs[p[0]][1]
            if p[0] == '<' and nextt == '/':
                p[0] = 'v'
            elif p[0] == '>' and nextt == '\\':
                p[0] = 'v'
            elif p[0] == '>' and nextt == '/':
                p[0] = '^'
            elif p[0] == '<' and nextt == '\\':
                p[0] = '^'
            elif p[0] == 'v' and nextt == '/':
                p[0] = '<'
            elif p[0] == 'v' and nextt == '\\':
                p[0] = '>'
            elif p[0] == '^' and nextt == '/':
                p[0] = '>'
            elif p[0] == '^' and nextt == '\\':
                p[0] = '<'
            content[p[1]][p[2]] = p[0]
        elif nextt == '+':
            mid.append((nextt, p[1] + dirs[p[0]][0], p[2] + dirs[p[0]][1]))
            if p[4] is None:
                p[4] = inter[p[0]]
            content[p[1]][p[2]] = p[4]
            p[1] = p[1] + dirs[p[0]][0]
            p[2] = p[2] + dirs[p[0]][1]
            p[0] = turn[p[0]][p[3] % 3]
            p[4] = '+'
            p[3] += 1
            content[p[1]][p[2]] = p[0]
        else:

            if p[4] == '+':
                content[p[1]][p[2]] = '+'
            elif p[4] in [chr(92), '/']:
                content[p[1]][p[2]] = p[4]
            else:
                content[p[1]][p[2]] = inter[p[0]]
            p[4] = nextt
            p[1] = p[1] + dirs[p[0]][0]
            p[2] = p[2] + dirs[p[0]][1]
            good = [x[0] for x in mid if (x[1], x[2]) == (p[1], p[2])]
            content[p[1]][p[2]] = [x[0] for x in mid if (x[1], x[2]) == (p[1], p[2])][0]
            positions = [x for x in positions if (x[1], x[2]) != (p[1], p[2])]
            mid = [x for x in mid if (x[1], x[2]) != (p[1], p[2])]
        positions.sort(key=lambda x: (x[1], x[2]))
        for x in content:
            print(''.join(x))
