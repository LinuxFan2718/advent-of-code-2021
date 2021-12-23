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
grow = 1
for iteration in range(iterations):
  if iteration % 10 == 0:
    print(iteration)
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

  for i in range(len(image[0])):
    for j in range(len(image)):
      if i == 0 and j == 0:
        raw_num = list('...') + list('.') + image[i][j:j+2] + list('.') + image[i+1][j:j+2]
      elif i == 0 and j > 0 and j < len(image) - 1:
        raw_num = list('...') + image[i][j:j+2] + image[i+1][j-1:j+2]
      elif i == 0 and j == len(image) - 1:
        raw_num = list('...') + image[i][j-1:j+1] + list('.') + image[i+1][j-1:j+1] + list('.')
      elif i > 0 and i < len(image[0]) - 1 and j == 0:
        raw_num = list('.') + image[i-1][j:j+2] + list('.') + image[i][j:j+2] + list('.') + image[i+1][j:j+2]
      elif i > 0 and i < len(image[0]) - 1 and j == len(image) - 1:
        raw_num = image[i-1][j-1:j+1] + list('.') + image[i][j-1:j+1] + list('.') + image[i+1][j-1:j+1] + list('.')
      elif i == len(image[0]) - 1 and j == 0:
        raw_num = list('.') + image[i-1][j:j+2] + list('.') + image[i][j:j+2] + list('...')
      elif i == len(image[0]) - 1 and j > 0 and j < len(image) - 1:
        raw_num = image[i-1][j-1:j+2] + image[i][j-1:j+2] + list('...')
      elif  i == len(image[0]) - 1 and j == len(image) - 1:
        raw_num = image[i-1][j-1:j+1] + list('.') + image[i][j-1:j+1] + list('.') + list('...')
      else:
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


num_lit_pixels = 0
for row in image:
  num_lit_pixels += row.count('#')

if DEBUG:
  for row in image:
    print(''.join(row))
  print()
print(num_lit_pixels)