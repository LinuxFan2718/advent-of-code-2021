filename = 'input10.txt'
f = open(filename)
illegal_characters = {
  ')': 0,
  ']': 0,
  '}': 0,
  '>': 0
}
while True:
  line = f.readline().strip()
  if line == '':
    break
  stack = []
  lefts = ['(','[','{','<']
  matches = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
  }
  for c in list(line):
    if c in lefts:
      stack.append(c)
    else:
      if len(stack) == 0 or stack[-1] != matches[c]:
        illegal_characters[c] += 1
        break
      elif stack[-1] == matches[c]:
        stack.pop()
  if len(stack) == 0:
    print(f"valid line {line}")
  else:
    print(f"incomplete line {stack} {line}")


points = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

score = 0
for key in illegal_characters:
  score += illegal_characters[key] * points[key]

print(f"score = {score}")