import re

dirs = {'N': [(-1, 0), (-2, 0)], 'E': [(0, 1), (0, 2)], 'S': [(1, 0), (2, 0)], 'W': [(0, -1), (0, -2)]}
doors = {'N': '-', 'S': '-', 'E': '|', 'W': '|'}
content = open('data.in').readline().strip()[1:-1].split('(')
print(content)

# grid = [['#' for _ in range(21)] for _ in range(21)]
# start_x, start_y = 10, 10
# grid[start_x][start_y] = 'X'
# route = [x for x in re.sub('([(|)])', ' ', route).split(' ') if x != '']
# print(route)
# for r in route:
#     for e in r:
#         door_x, door_y = start_x + dirs[e][0][0], start_y + dirs[e][0][1]
#         room_x, room_y = start_x + dirs[e][1][0], start_y + dirs[e][1][1]
#         grid[door_x][door_y] = doors[e]
#         grid[room_x][room_y] = '.'
#         start_x, start_y = room_x, room_y
#
# for line in grid:
#     print(line)
