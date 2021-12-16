filename = 'input13.txt'
f = open(filename)
paper = [['.']]
visible_dots = []

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

foldings = []
while True:
  line = f.readline().strip()
  if line == '':
    break
  foldings.append(line[11:])

this_visible_dots = len([dot for l in paper for dot in l if dot == '#'])
visible_dots.append(this_visible_dots)

for folding in foldings:
  foldaxis = folding[0]
  foldn = int(folding[2:])

  if foldaxis == 'y':
    new_paper = []
    for i in range(foldn):
      new_row = paper[i]
      row_to_add = paper[-i-1]
      for y in range(len(new_row)):
        if row_to_add[y] == '#':
          new_row[y] = '#'
      new_paper.append(new_row)

  if foldaxis == 'x':
    new_paper = []
    for i in range(len(paper)):
      new_row = paper[i][0:foldn]
      row_to_add = paper[i][-1:-foldn-1:-1]
      for y in range(foldn):
        if row_to_add[y] == '#':
          new_row[y] = '#'
      new_paper.append(new_row)

  paper = new_paper
  
  print()
  for row in paper:
    print(''.join(row))
  print()

  this_visible_dots = len([dot for l in paper for dot in l if dot == '#'])
  visible_dots.append(this_visible_dots)

print()
for row in paper:
  print(''.join(row))
print()
print(visible_dots)