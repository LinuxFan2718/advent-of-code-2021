filename = 'input5-test.txt'
f = open(filename)
vents = [[0]]

# build up diagram of vents
while True:
  vent_raw = f.readline().strip() # 0,9 -> 5,9
  if vent_raw == '':
    break
  vent_pair = [x.strip().split(',') for x in vent_raw.split(' -> ')]
  x1, y1 = [int(n) for n in vent_pair[0]]
  x2, y2 = [int(n) for n in vent_pair[1]]

  if x1 == x2 or y1 == y2:
    small_y, large_y = None, None
    if y1 < y2:
      small_y = y1
      large_y = y2
    elif y2 <= y1:
      small_y = y2
      large_y = y1
    small_x, large_x = None, None
    if x1 < x2:
      small_x = x1
      large_x = x2
    elif x2 <= x1:
      small_x = x2
      large_x = x1
    # if vents is too small, grow it
    if large_x >= len(vents):
      i = len(vents)
      empty_row = [0] * len(vents[0])
      while i <= large_x:
        empty_row_dup = empty_row[:]
        vents.append(empty_row_dup)
        i += 1
    if large_y > len(vents[0]):
      zeroes_to_add = [0] * (large_y - len(vents[0]) + 1)
      for n in range(len(vents)):
        vents[n] = vents[n] + zeroes_to_add
  # increase numbers for this line
  if x1 == x2:
    for y in range(small_y, large_y+1):
      vents[x1][y] += 1
  if y1 == y2:
    for x in range(small_x, large_x+1):
      vents[x][y1] += 1

# determine the number of points where at least two lines overlap
overlap_points = 0
for row in vents:
  for point in row:
    if point > 1:
      overlap_points +=1

print(overlap_points)
