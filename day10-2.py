filename = 'input10.txt'
f = open(filename)
scores = []
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
  points = {
  '(': 1,
  '[': 2,
  '{': 3,
  '<': 4
}
  score = 0
  corrupted = False
  for c in list(line):
    if c in lefts:
      stack.append(c)
    else:
      if len(stack) == 0 or stack[-1] != matches[c]:
        corrupted = True
        break
      elif stack[-1] == matches[c]:
        stack.pop()
  if not corrupted:
    while len(stack) > 0:
      score *= 5
      score += points[stack.pop()]
    scores.append(score)

scores.sort()
print(f"scores = {scores}")
print(f"middle score = {scores[len(scores)//2]}")