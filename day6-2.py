from collections import Counter
filename = 'input6.txt'
f = open(filename)
fish_raw = f.readline().strip()
fish_str = fish_raw.split(',')
fish = [int(x) for x in fish_str]
fish_dict = dict(Counter(fish))
for i in range(9):
  if i in fish_dict:
    pass
  else:
    fish_dict[i] = 0
days_to_simulate = 256
for i in range(days_to_simulate):
  #print(i)
  num_new_fish = fish_dict[0]
  new_fish_dict = {}
  for j in range(8):
    new_fish_dict[j] = fish_dict[j+1]
  new_fish_dict[6] += num_new_fish
  new_fish_dict[8] = num_new_fish
  fish_dict = new_fish_dict
  
print(f"{sum(list(fish_dict.values()))}")
pass