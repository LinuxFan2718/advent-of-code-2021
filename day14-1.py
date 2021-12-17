from collections import Counter
import datetime

filename = 'input14-test.txt'
f = open(filename)
polymer_template = f.readline().strip()
_skip = f.readline().strip()
pair_insertion = {}
while True:
  line = f.readline().strip()
  if line == '':
    break
  key, value = line.split(' -> ')
  pair_insertion[key] = value

steps = 10
print(f"Template:     {polymer_template}")
for step in range(1, steps + 1):
  start_time = datetime.datetime.now()
  new_polymer_template = polymer_template[0]
  for i in range(len(polymer_template) - 1):
    pair = polymer_template[i:i+2]
    if pair in pair_insertion:
      new_polymer_template += pair_insertion[pair]
    new_polymer_template += polymer_template[i + 1]
  polymer_template = new_polymer_template
  print(f"After step {step}: {datetime.datetime.now() - start_time} {len(polymer_template)}")

elements = dict(Counter(polymer_template))
sorted_elements = {v: k for k, v in sorted(elements.items(), key=lambda item: item[1])}
difference = max(sorted_elements) - min(sorted_elements)
print(difference)