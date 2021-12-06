from collections import Counter
filename = 'input3.txt'
inputs = []
with open(filename) as file:
  for line in file:
    inputs.append(line.strip())
# oxygen
oxygen = None
oinputs = inputs[:]
for i in range(len(inputs[0])):
  this_digit = [x[i] for x in oinputs]
  this_tally = Counter(this_digit)
  if this_tally["0"] > this_tally["1"]:
    oinputs = [x for x in oinputs if x[i] == "0"]
  else:
    oinputs = [x for x in oinputs if x[i] == "1"]
  if len(oinputs) == 1:
    oxygen = oinputs[0]
    break

# co2
co2 = None
cinputs = inputs[:]
for i in range(len(inputs[0])):
  this_digit = [x[i] for x in cinputs]
  this_tally = Counter(this_digit)
  if this_tally["0"] > this_tally["1"]:
    cinputs = [x for x in cinputs if x[i] == "1"]
  else:
    cinputs = [x for x in cinputs if x[i] == "0"]
  if len(cinputs) == 1:
    co2 = cinputs[0]
    break

oxygen_int = int(oxygen, 2)
co2_int = int(co2, 2)
print(f"oxygen {oxygen} {oxygen_int}")
print(f"co2    {co2} {co2_int}")
print(f"quotient {oxygen_int * co2_int}")
pass
