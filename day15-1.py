import random
filename = 'input15-test.txt'
f = open(filename)
risk_level_map = []
visited = []
while True:
  line = f.readline().strip()
  if line == '':
    break
  row = [int(x) for x in list(line)]
  risk_level_map.append(row)
  visited.append([False] * len(row))

total_risk = 0
x, y = 0, 0
destination_x = len(risk_level_map) - 1
destination_y = len(risk_level_map[0]) - 1

while not (x == destination_x and y == destination_y):
  moves = []
  if x > 0 and visited[x-1][y] == False: #up
    pass
    #moves.append([x-1, y])
  if y > 0 and visited[x][y-1] == False: # left
    moves.append([x, y -1])
  if x < len(risk_level_map) - 1 and visited[x+1][y] == False: #down
    moves.append([x+1, y])
  if y < len(risk_level_map[0]) - 1 and visited[x][y+1] == False: #right
    moves.append([x, y+1])
  move = random.choice(moves)
  x, y = move
  visited[x][y] = True
  total_risk += risk_level_map[x][y]

print(f"total risk = {total_risk}")
for i in range(len(risk_level_map)):
  for j in range(len(risk_level_map[0])):
    if visited[i][j]:
      print('\033[1m' + str(risk_level_map[i][j]) + '\033[0m', end = '')
    else:
      print(str(risk_level_map[i][j]), end = '')
  print()