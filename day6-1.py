filename = 'input6.txt'
f = open(filename)
fish_raw = f.readline().strip()
fish_str = fish_raw.split(',')
fish = [int(x) for x in fish_str]
days_to_simulate = 80
for i in range(days_to_simulate):
  num_new_fish = 0
  for j in range(len(fish)):
    if fish[j] == 0:
      num_new_fish += 1
      fish[j] = 6
    else:
      fish[j] -= 1
  fish = fish + [8] * num_new_fish
print(f"{len(fish)}")
pass