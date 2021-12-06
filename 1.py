filename = 'input1.txt'
increases = 0
previous_value = float('inf')
with open(filename) as file:
    for line in file:
        num = int(line.strip())
        if num > previous_value:
          increases += 1
        previous_value = num
print(increases)
