import math
filename = 'input9.txt'
f = open(filename)
floor = []
visited = []
while True:
  line = f.readline().strip()
  if line == '':
    break
  nums = [int(x) for x in list(line)]
  floor.append(nums)
  visited.append([False] * len(nums))

# spider elements, marking them visited
def spider(i, j):
  if visited[i][j] == True:
    return 0
  visited[i][j] = True
  if floor[i][j] == 9:
    return 0

  left = spider(i, j-1) if j - 1 >= 0 else 0
  right = spider(i, j+1) if j+1 < len(floor[0]) else 0
  up = spider(i-1, j) if i - 1 >= 0 else 0
  down = spider(i+1, j) if i+1 < len(floor) else 0
  return 1 + left + right + up + down

basin_sizes = []
for i in range(len(floor)):
  for j in range(len(floor[0])):
    if visited[i][j] == True:
      next
    basin_size = spider(i, j)
    if basin_size > 0:
      basin_sizes.append(basin_size)

basin_sizes.sort()
three_largest_basin_sizes = basin_sizes[-3:]
answer = math.prod(three_largest_basin_sizes)
print(f"answer = {answer}")
pass