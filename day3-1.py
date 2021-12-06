gamma = 0
epsilon = 0
filename = 'input3.txt'
tally = []
num_lines = 0
with open(filename) as file:
  for line in file:
    num_lines += 1
    if tally == []:
      for i in range(len(line) - 1):
        tally.append(0)
    num = int(line.strip(), 2)
    i = 0
    while num > 0:
      if num & 1 == 1:
        tally[i] += 1
      i += 1
      num >>= 1

tally.reverse()
gamma_list = ["1" if x-(num_lines/2) > 0 else "0" for x in tally]
gamma_binstr = "".join(gamma_list)
gamma = int(gamma_binstr,2)
epsilon_list = ["0" if x-(num_lines/2) > 0 else "1" for x in tally]
epsilon_binstr = "".join(epsilon_list)
epsilon = int(epsilon_binstr,2)
print(f"gamma   {gamma_binstr} == {gamma}")
print(f"epsilon {epsilon_binstr} == {epsilon}")
print(f"quotient = {gamma * epsilon}")
pass