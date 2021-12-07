filename = 'input7.txt'
numbers = []
f = open(filename)
raw_numbers = f.readline()
nums = [int(x) for x in raw_numbers.strip().split(',')]
nums.sort()
best_position = 0
best_position_fuel = float('inf')
for n in range(nums[0], nums[-1]):
  total_fuel = sum([sum(range(abs(n-x)+1)) for x in nums])
  if total_fuel < best_position_fuel:
    best_position = n
    best_position_fuel = total_fuel
print(f"best position {best_position} fuel {best_position_fuel}")