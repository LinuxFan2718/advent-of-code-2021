filename = 'input9.txt'
f = open(filename)
floor = []
while True:
  line = f.readline().strip()
  if line == '':
    break
  nums = [int(x) for x in list(line)]
  floor.append(nums)

low_points = []
for i in range(len(floor)):
  for j in range(len(floor[0])):
    left = floor[i][j-1] if j - 1 >= 0 else float('inf')
    right = floor[i][j+1] if j+1 < len(floor[0]) else float('inf')
    up = floor[i-1][j] if i - 1 >= 0 else float('inf')
    down = floor[i+1][j] if i+1 < len(floor) else float('inf')

    if all([floor[i][j] < x for x in [left, right, up, down]]):
      low_points.append(floor[i][j])

risk_levels = sum([x+1 for x in low_points])
print(f"risk levels = {risk_levels}")
pass
