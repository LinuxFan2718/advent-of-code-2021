horizontal = 0
depth = 0
aim = 0
filename = 'input2.txt'
with open(filename) as file:
  for line in file:
    sline = line.strip()
    direction, amount = sline.split(" ")
    num = int(amount)
    if direction == "forward":
      horizontal += num
      depth += aim * num
    elif direction == "down":
      aim += num
    elif direction == "up":
      aim -= num

    if depth < 0:
      print(f"{depth} {sline}")

print(f"horizontal = {horizontal}")
print(f"depth      = {depth}")
print(f"quotient   = {horizontal * depth}")
