from collections import Counter

filename = 'input14.txt'
f = open(filename)
polymer_template = f.readline().strip()
polymer_pair_count = {}
for i in range(len(polymer_template) - 1):
  this_pair = polymer_template[i:i+2]
  if this_pair in polymer_pair_count:
    polymer_pair_count[this_pair] += 1
  else:
    polymer_pair_count[this_pair] = 1

_skip = f.readline().strip()
pair_insertion = {}
while True:
  line = f.readline().strip()
  if line == '':
    break
  key, value = line.split(' -> ')
  pair_insertion[key] = value

steps = 40
print(f"Template:     {polymer_template}")
for step in range(1, steps + 1):
  new_polymer_pair_count = {}
  for key in polymer_pair_count:
    if key in pair_insertion:
      num_to_add = polymer_pair_count[key]
      left =  key[0] + pair_insertion[key]
      right = pair_insertion[key] + key[1]
      if left in new_polymer_pair_count:
        new_polymer_pair_count[left] += num_to_add
      else:
        new_polymer_pair_count[left] = num_to_add
      if right in new_polymer_pair_count:
        new_polymer_pair_count[right] += num_to_add
      else:
        new_polymer_pair_count[right] = num_to_add
    else:
      new_polymer_pair_count[key] = num_to_add
  polymer_pair_count = new_polymer_pair_count

elements = {}
elements[polymer_template[0]] = 1
elements[polymer_template[-1]] = 1
for key in polymer_pair_count:
  left = key[0]
  right = key[1]
  for x in [left, right]:
    if x in elements:
      elements[x] += polymer_pair_count[key]
    else:
      elements[x] = polymer_pair_count[key]

sorted_elements = {(v//2): k for k, v in sorted(elements.items(), key=lambda item: item[1])}
difference = max(sorted_elements) - min(sorted_elements)
print(difference)
pass