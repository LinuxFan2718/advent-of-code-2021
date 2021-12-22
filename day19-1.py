filename = 'input19-test.txt'
f = open(filename)
scanners = []
scanner_num = 0
while True:
  line = f.readline()
  if line == '':
    break
  line = line.strip()
  if line == '':
    continue
  if line[0:3] == '---':
    if line[13] == ' ':
      scanner_num = int(line[12])
    else:
      scanner_num = int(line[12:14])
    scanners.append([])
  else:
    x,y,z = [int(n) for n in line.split(',')]
    scanners[scanner_num].append([x,y,z])

# compute distance from each other
distances = []
for x in range(len(scanners)):
  scanner = scanners[x]
  distances.append([None] * len(scanner))
  for i in range(len(scanner)):
    distances[x][i] = [None] * len(scanner)
    for j in range(len(scanner)):
      x1, y1, z1 = scanner[i]
      x2, y2, z2 = scanner[j]
      dist_squared = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2 
      distances[x][i][j] = dist_squared
pass


# look for identical distances