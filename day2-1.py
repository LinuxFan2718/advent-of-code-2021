horizontal = 0
depth = 0
filename = 'input2.txt'
with open(filename) as file:
  for line in file:
    sline = line.strip()
    direction, amount = sline.split(" ")
    num = int(amount)
    if direction == "forward":
      horizontal += num
    elif direction == "down":
      depth += num
    elif direction == "up":
      depth -= num
      if depth < 0:
        print(f"{depth} {sline}")

print(f"horizontal = {horizontal}")
print(f"depth      = {depth}")
print(f"quotient   = {horizontal * depth}")
