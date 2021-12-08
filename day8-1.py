filename = 'input8.txt'

f = open(filename)

instances_uniq_digits = 0
while True:
  line = f.readline()
  if line == '':
    break
  c = [x.strip() for x in line.split('|')]
  e = [''.join(sorted(x)) for x in c[1].split(' ')]
  g = [len(x) for x in e]
  # the digits 1, 4, 7, and 8
  h = [x for x in g if x in [2,3,4,7]]
  instances_uniq_digits += len(h)

print(f"instances of 2,3,4,7 = {instances_uniq_digits}")

