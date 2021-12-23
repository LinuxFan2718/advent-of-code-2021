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
for _ in range(iterations):
  grow = 2
  width = len(image[0])
  height = len(image)
  for i in range(height):
    image[i] = ['.'] * grow + image[i] + ['.'] * grow

  for _ in range(grow):
    image.insert(0, ['.'] * (width+2*grow))
  for _ in range(grow):
    image.append(['.'] * (width+2*grow))

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
  image = new_image

num_lit_pixels = 0
for row in image:
  num_lit_pixels += row.count('#')

print(num_lit_pixels)