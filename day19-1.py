from collections import Counter
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
dist_scanner = {}
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
      if dist_squared > 0 and i > j:
        if dist_squared in dist_scanner:
          dist_scanner[dist_squared].append([x,i,j])
        else:
          dist_scanner[dist_squared] = [[x,i,j]]
matches = [v for k,v in dist_scanner.items() if len(v) > 1]
# matches12 = [x for x in matches if x[0][0] == 0 and x[1][0] == 1]
pass
candidate_matches = {}
for x in range(len(matches)):
  match = matches[x]
  for i in range(len(match)):
    scanner_n = match[i][0]
    corresponding_beacons = []
    other_matches_k = list(range(len(match)))
    other_matches_k.remove(i)
    for k in other_matches_k:
      corresponding_beacons.append( [ match[k][0], match[k][1] ] )
      corresponding_beacons.append( [ match[k][0], match[k][2] ] )
    for j in [1, 2]:
      key = tuple([match[i][0], match[i][j]])
      if key in candidate_matches:
        for beacon in corresponding_beacons:
          candidate_matches[key].append(beacon)
      else:
        candidate_matches[key] = corresponding_beacons

confirmed_matches = {}
for key in candidate_matches:
  c = Counter([tuple(z) for z in candidate_matches[key]])
  d = c.most_common(2)
  
  pass
# determine coordinates of the scanners