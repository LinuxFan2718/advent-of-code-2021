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

pass