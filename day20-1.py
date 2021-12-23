DEBUG = True
filename = 'input20-test.txt'
f = open(filename)
lookup = ''
while True:
  line = f.readline().strip()
  if line == '':
    break
  lookup += line

image = []
while True:
  line = f.readline().strip()
  if line == '':
    break
  image.append(list(line))


iterations = 2
grow = 6
for _ in range(iterations):
  width = len(image[0])
  height = len(image)
  for i in range(height):
    image[i] = ['.'] * grow + image[i] + ['.'] * grow

  for _ in range(grow):
    image.insert(0, ['.'] * (width+2*grow))
  for _ in range(grow):
    image.append(['.'] * (width+2*grow))

  if False:
    for row in image:
      print(''.join(row))
    print()

  new_image = []
  for row in image:
    new_image.append(row[:])

  for i in range(1, len(image[0]) - 1):
    for j in range(1, len(image) - 1):
      raw_num = image[i-1][j-1:j+2] + image[i][j-1:j+2] + image[i+1][j-1:j+2]
      num = 0
      for k in range(len(raw_num)):
        num <<= 1
        if raw_num[k] == '#':
          num +=1
      new_image[i][j] = lookup[num]
  image = []
  for row in new_image:
    image.append(row[:])


# trim edge
trimmed_image = []
for i in range(grow + 2, len(image) - grow - 2):
  trimmed_image.append(image[i][grow+2:-grow-2])

num_lit_pixels = 0
for row in trimmed_image:
  num_lit_pixels += row.count('#')

if DEBUG:
  for row in trimmed_image:
    print(''.join(row))
  print()

print(num_lit_pixels)