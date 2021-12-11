filename = 'input11.txt'
f = open(filename)
energy_levels = []
while True:
  line = f.readline().strip()
  if line == '':
    break
  energy_levels.append([int(x) for x in list(line)])

steps_to_simulate = 500
flashes = 0
step = 0
while step < steps_to_simulate:
  step += 1
  for i in range(len(energy_levels)):
    energy_levels[i] = [x + 1 for x in energy_levels[i]]
  
  while any([x > 9 for row in energy_levels for x in row]):
    for i in range(len(energy_levels)):
      for j in range(len(energy_levels[0])):
        if energy_levels[i][j] > 9:
          flashes += 1
          energy_levels[i][j] = float('-inf')
          if i - 1 >= 0 and j - 1 >= 0:
            energy_levels[i-1][j-1] += 1
          if i - 1 >= 0:
            energy_levels[i-1][j] += 1
          if i - 1 >= 0 and j + 1 < len(energy_levels[0]):
            energy_levels[i-1][j+1] += 1
          if j - 1 >= 0:
            energy_levels[i][j-1] += 1  
          if j + 1 < len(energy_levels[0]):
            energy_levels[i][j+1] += 1
          if i + 1 < len(energy_levels) and j - 1 >= 0:
            energy_levels[i+1][j-1] += 1
          if i + 1 < len(energy_levels):
            energy_levels[i+1][j] += 1
          if i + 1 < len(energy_levels) and j + 1 < len(energy_levels[0]):
            energy_levels[i+1][j+1] += 1

  all_flashed = True
  for i in range(len(energy_levels)):
    for j in range(len(energy_levels[0])):
      if energy_levels[i][j] == float('-inf'):
        energy_levels[i][j] = 0
      else:
        all_flashed = False
  if all_flashed:
    print(f"all flashed on step {step}")

print(f"flashes = {flashes}")
