filename = 'input13-test-1.txt'
f = open(filename)
paper = [['.']]
while True:
  line = f.readline().strip()
  if line == '':
    break
  x, y = [int(n) for n in line.split(',')]
  # paper[y][x]
  if y >= len(paper):
    for i in range(y - len(paper) + 1):
      new_row = ['.'] * len(paper[0])
      paper.append(new_row)
  if x >= len(paper[0]):
    dots_to_add = ['.'] * (x - len(paper[0]) + 1)
    for i in range(len(paper)):
      replacement_row = paper[i] + dots_to_add
      paper[i] = replacement_row
  paper[y][x] = '#'

for row in paper:
  print(''.join(row))

folding = []
while True:
  line = f.readline().strip()
  if line == '':
    break
  folding.append(line)

pass