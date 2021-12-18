import math
filename = 'input15.txt'
f = open(filename)
risk_level_map = []
visited = []
dist = []
prev = []
while True:
  line = f.readline().strip()
  if line == '':
    break
  row = [int(x) for x in list(line)]
  risk_level_map.append(row)
  visited.append([False] * len(row))
  dist.append([math.inf] * len(row))
  prev.append([None] * len(row))

dist[0][0] = 0

destination_x = len(risk_level_map) - 1
destination_y = len(risk_level_map[0]) - 1

while not visited[destination_x][destination_y]:
  unexplored_vertices = []
  for i in range(len(dist)):
    for j in range(len(dist[0])):
      if not visited[i][j]:
        unexplored_vertices.append([i, j])
  least_valued_unexplored_vertex = unexplored_vertices[0]
  for i in range(1, len(unexplored_vertices)): # find least valued
    cx, cy = unexplored_vertices[i]
    lx, ly = least_valued_unexplored_vertex
    if dist[cx][cy] < dist[lx][ly]:
      least_valued_unexplored_vertex = unexplored_vertices[i]
  v = least_valued_unexplored_vertex
  vx, vy = v

  visited[vx][vy] = True
  moves = []
  if vx > 0 and visited[vx-1][vy] == False: #up
    moves.append([vx-1, vy])
  if vy > 0 and visited[vx][vy-1] == False: # left
    moves.append([vx, vy -1])
  if vx < len(risk_level_map) - 1 and visited[vx+1][vy] == False: #down
    moves.append([vx+1, vy])
  if vy < len(risk_level_map[0]) - 1 and visited[vx][vy+1] == False: #right
    moves.append([vx, vy+1])
  for move in moves:
    mx, my = move
    if dist[vx][vy] + risk_level_map[mx][my] < dist[mx][my]:
      dist[mx][my] = dist[vx][vy] + risk_level_map[mx][my]
      prev[mx][my] = [vx, vy]

print(f"lowest total risk = {dist[destination_x][destination_y]}")
# print(f"best solution {this_total_risk}")
# solution = this_condition
# for i in range(len(risk_level_map)):
#   for j in range(len(risk_level_map[0])):
#     if this_visited[i][j]:
#       print('\033[91m' + str(risk_level_map[i][j]) + '\033[0m', end = '')
#     else:
#       print(str(risk_level_map[i][j]), end = '')
#   print()
# print()