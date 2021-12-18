import random
filename = 'input15.txt'
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
visited[x][y] = True
destination_x = len(risk_level_map) - 1
destination_y = len(risk_level_map[0]) - 1

initial_condition = {
  'position': [0,0],
  'visited':  visited,
  'total_risk': 0
}
stack = [initial_condition]
failed = []
lowest_risk = float('inf')

while len(stack) > 0:
  condition = stack.pop()
  if condition in failed:
    continue
  x, y = condition['position']
  visited = condition['visited']
  total_risk = condition['total_risk']
  if total_risk >= lowest_risk:
    failed.append(condition)
    continue
  
  moves = []
  # if x > 0 and visited[x-1][y] == False: #up
  #   moves.append([x-1, y])
  # if y > 0 and visited[x][y-1] == False: # left
  #   moves.append([x, y -1])
  if x < len(risk_level_map) - 1 and visited[x+1][y] == False: #down
    moves.append([x+1, y])
  if y < len(risk_level_map[0]) - 1 and visited[x][y+1] == False: #right
    moves.append([x, y+1])
  if len(moves) == 0:
    failed.append(condition)

  for move in moves:
    this_x, this_y = move
    this_visited = [row[:] for row in visited]
    this_visited[this_x][this_y] = True
    this_total_risk = total_risk + risk_level_map[this_x][this_y]
    this_condition = {
      'position': [this_x, this_y],
      'visited': this_visited,
      'total_risk': this_total_risk
    }
    if this_x == destination_x and this_y == destination_y and this_total_risk < lowest_risk:
      lowest_risk = this_total_risk
      print(f"best solution {this_total_risk}")
      solution = this_condition
      for i in range(len(risk_level_map)):
        for j in range(len(risk_level_map[0])):
          if this_visited[i][j]:
            print('\033[91m' + str(risk_level_map[i][j]) + '\033[0m', end = '')
          else:
            print(str(risk_level_map[i][j]), end = '')
        print()
      print()
    elif this_total_risk < lowest_risk:
      stack.append(this_condition)

print(f"lowest total risk = {lowest_risk}")