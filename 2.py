filename = 'input1.txt'
increases = 0
queue = []
previous_value = float('inf')
with open(filename) as file:
  for line in file:
    num = int(line.strip())
    queue.insert(0, num)
    if len(queue) > 3:
      queue.pop()
    elif len(queue) < 3:
      continue
    this_sum = 0
    for x in queue:
      this_sum += x
    if this_sum > previous_value:
      increases += 1
    previous_value = this_sum

print(increases)
