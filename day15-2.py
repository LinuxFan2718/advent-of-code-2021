import math
import datetime
filename = 'input15-test.txt'
f = open(filename)
risk_level_map = []


while True:
  line = f.readline().strip()
  if line == '':
    break
  row = [int(x) for x in list(line)]
  sub_row = row[:]
  new_row = row[:]
  for i in range(1, 5):
    sub_row = [x + 1 if x + 1 < 10 else 1 for x in sub_row]
    new_row += sub_row
  row = new_row
  risk_level_map.append(row)

# repeat the risk level map four more times adding +1
original_length = len(risk_level_map)
for i in range(original_length, 5*original_length):
  source_row = risk_level_map[i-original_length]
  new_row = [x + 1 if x + 1 < 10 else 1 for x in source_row]
  risk_level_map.append(new_row)

visited = []
dist = []
prev = []
for row in risk_level_map:
  visited.append([False] * len(row))
  dist.append([math.inf] * len(row))
  prev.append([None] * len(row))

dist[0][0] = 0

destination_x = len(risk_level_map) - 1
destination_y = len(risk_level_map[0]) - 1
runs = 0
start_time = datetime.datetime.now()

unexplored_vertices = []
for i in range(len(dist)):
  for j in range(len(dist[0])):
    if not visited[i][j]:
      unexplored_vertices.append([i, j])

while not visited[destination_x][destination_y]:
  runs += 1
  if runs % 500 == 0:
    lst = [x for l in visited for x in l]
    visited_amount = len([visited_already for visited_already in lst if visited_already]) / len(lst)
    print(f"After runs {runs}: visited {visited_amount} in {datetime.datetime.now() - start_time}")

  least_valued_unexplored_vertex = unexplored_vertices[0]
  visited_vertex_i = 0
  for i in range(1, len(unexplored_vertices)): # find least valued
    cx, cy = unexplored_vertices[i]
    lx, ly = least_valued_unexplored_vertex
    if dist[cx][cy] < dist[lx][ly]:
      least_valued_unexplored_vertex = unexplored_vertices[i]
      visited_vertex_i = i
  del unexplored_vertices[visited_vertex_i]
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
