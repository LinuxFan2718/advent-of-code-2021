def list_numbers_in_order(l, current_i=[]):
  idx = []
  for i in range(len(l)):
    if isinstance(l[i], int):
      idx += [current_i + [i]]
    elif isinstance(l[i], list):
      this_i = current_i + [i]
      idx += list_numbers_in_order(l[i], this_i)
  return idx

def explode(smallfish_number):
  idx = list_numbers_in_order(smallfish_number)
  x = -1
  stop = False
  while not stop and x + 1 < len(idx):
    x += 1
    if len(idx[x]) == 5:
      i, j, k, m = idx[x][0], idx[x][1], idx[x][2], idx[x][3]
      left, right = smallfish_number[i][j][k][m]
      smallfish_number[i][j][k][m] = 0
      if x > 0:
        left_i = idx[x - 1]
        if len(left_i) == 1:
          smallfish_number[left_i[0]] += left
        elif len(left_i) == 2:
          smallfish_number[left_i[0]][left_i[1]] += left
        elif len(left_i) == 3:
          smallfish_number[left_i[0]][left_i[1]][left_i[2]] += left
        elif len(left_i) == 4:
          smallfish_number[left_i[0]][left_i[1]][left_i[2]][left_i[3]] += left
      if x + 2 < len(idx):
        right_i = idx[x + 2]
        if len(right_i) == 1:
          smallfish_number[right_i[0]] += right
        elif len(right_i) == 2:
          smallfish_number[right_i[0]][right_i[1]] += right
        elif len(right_i) == 3:
          smallfish_number[right_i[0]][right_i[1]][right_i[2]] += right
        elif len(right_i) == 4:
          smallfish_number[right_i[0]][right_i[1]][right_i[2]][right_i[3]] += right
        elif len(right_i) == 5:
          smallfish_number[right_i[0]][right_i[1]][right_i[2]][right_i[3]][right_i[4]] += right
      stop = True
  return stop

def split(smallfish_number):
  idx = list_numbers_in_order(smallfish_number)
  x = -1
  stop = False
  while not stop and x + 1 < len(idx):
    x += 1
    val = None
    if len(idx[x]) == 1:
      val = smallfish_number[idx[x][0]]
    elif len(idx[x]) == 2:
      val = smallfish_number[idx[x][0]][idx[x][1]]
    elif len(idx[x]) == 3:
      val = smallfish_number[idx[x][0]][idx[x][1]][idx[x][2]]
    elif len(idx[x]) == 4:
      val = smallfish_number[idx[x][0]][idx[x][1]][idx[x][2]][idx[x][3]]
    if val >= 10:
      stop = True
      left = val // 2
      right = val // 2 if val % 2 == 0 else 1 + (val // 2)
      newpair = [left, right]
      if len(idx[x]) == 1:
        smallfish_number[idx[x][0]] = newpair
      elif len(idx[x]) == 2:
        smallfish_number[idx[x][0]][idx[x][1]] = newpair
      elif len(idx[x]) == 3:
        smallfish_number[idx[x][0]][idx[x][1]][idx[x][2]] = newpair
      elif len(idx[x]) == 4:
        smallfish_number[idx[x][0]][idx[x][1]][idx[x][2]][idx[x][3]] = newpair
  return stop

def magnitude(smallfish_number):
  if isinstance(smallfish_number, int):
    return smallfish_number
  elif isinstance(smallfish_number, list):
    return 3 * magnitude(smallfish_number[0]) + 2 * magnitude(smallfish_number[1])

def addition(smallfish_number1, smallfish_number2):
  ans = [smallfish_number1, smallfish_number2]

  return ans
  
def reduce(s_number):
  smallfish_number = s_number[:]
  did_split = False
  did_explode = explode(smallfish_number)
  if not did_explode:
    did_split = split(smallfish_number)
  if did_explode or did_split:
    reduce(smallfish_number)
  return smallfish_number

filename = 'input18.txt'
f = open(filename)
snailfish_numbers = []
while True:
  line = f.readline().strip()
  if line == '':
    break
  snailfish_numbers.append(eval(line))
# snailfish_numbers = [
#   [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
#   [[[5,[2,8]],4],[5,[[9,9],0]]],
#   [6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
#   [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
#   [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
#   [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
#   [[[[5,4],[7,7]],8],[[8,3],8]],
#   [[9,3],[[9,9],[6,[4,9]]]],
#   [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
#   [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
# ]
largest_magnitude = -1
import itertools
for tuple in list(itertools.permutations(range(len(snailfish_numbers)), r=2)):
  filename = 'input18.txt'
  f = open(filename)
  snailfish_numbers = []
  while True:
    line = f.readline().strip()
    if line == '':
      break
    snailfish_numbers.append(eval(line))
  this_sum = None
  this_sum = addition(snailfish_numbers[tuple[0]], snailfish_numbers[tuple[1]])
  new_sum = reduce(this_sum)
  this_magnitude = magnitude(new_sum)
  if this_magnitude > largest_magnitude:
    largest_magnitude = this_magnitude
  if this_magnitude > 3993:
    print(f"wrong {tuple}")

print(f"largest magnitude = {largest_magnitude}. (example 3993)")
print(f"{snailfish_numbers[6]}")
print(f"{snailfish_numbers[0]}")
this_sum = addition(snailfish_numbers[6], snailfish_numbers[0])
reduce(this_sum)
this_magnitude = magnitude(this_sum)
print(this_magnitude)

# snailfish_numbers = [
  # [1,1],
  # [2,2],
  # [3,3],
  # [4,4],
  # [5,5],
  # [6,6]
  # [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
  # [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
  # [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
  # [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
  # [7,[5,[[3,8],[1,4]]]],
  # [[2,[2,2]],[8,[8,1]]],
  # [2,9],
  # [1,[[[9,3],9],[[9,0],[0,7]]]],
  # [[[5,[7,4]],7],1],
  # [[[[4,2],2],6],[8,7]]
  # [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
  # [[[5,[2,8]],4],[5,[[9,9],0]]],
  # [6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
  # [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
  # [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
  # [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
  # [[[[5,4],[7,7]],8],[[8,3],8]],
  # [[9,3],[[9,9],[6,[4,9]]]],
  # [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
  # [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
# ]

# running_sum = snailfish_numbers[0]
# for x in range(1, len(snailfish_numbers)):
#   print(f"  {running_sum}")
#   print(f"+ {snailfish_numbers[x]}")
#   running_sum = addition(running_sum[:], snailfish_numbers[x])
#   reduce(running_sum)
#   print(f"= {running_sum}")
#   print()

# ans = [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
# print(f"{running_sum == ans}")
# print(f"{magnitude(running_sum) == 4140}")

# l1 = [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]
# l2 = [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]]
# l3 = addition(l1, l2)
# reduce(l3)
# print(f"{l3}")

# print(f"{running_sum == [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]}")
# print(f"{running_sum}")
# print(f"{[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]}")

# res = magnitude([9,1])
# print(f"{res == 29} {res} == {29}")
# res = magnitude([1,9])
# print(f"{res == 21} {res} == {21}")
# res = magnitude([[9,1],[1,9]])
# print(f"{res == 129} {res} == {129}")
# res = magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])
# print(f"{res == 3488} {res} == {3488}")
# smallfish_number = [[[[[9,8],1],2],3],4]
# explode(smallfish_number)
# print(f"{smallfish_number == [[[[0,9],2],3],4]}  {smallfish_number} == {[[[[0, 9], 2], 3], 4]}")

# smallfish_number = [7,[6,[5,[4,[3,2]]]]]
# reduce(smallfish_number)
# print(f"{smallfish_number == [7,[6,[5,[7,0]]]]}")

# smallfish_number = [[6,[5,[4,[3,2]]]],1]
# explode(smallfish_number)
# print(f"{smallfish_number == [[6,[5,[7,0]]],3]} {smallfish_number} == [[6, [5, [7, 0]]], 3]")

# smallfish_number = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
# explode(smallfish_number)
# print(f"{smallfish_number == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]}")

# smallfish_number = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
# explode(smallfish_number)
# print(f"{smallfish_number == [[3,[2,[8,0]]],[9,[5,[7,0]]]]}")

# smallfish_number = [[[[0,7],4],[15,[0,13]]],[1,1]]
# split(smallfish_number)
# print(f"{smallfish_number == [[[[0,7],4],[[7,8],[0,13]]],[1,1]]} {smallfish_number} == {[[[[0,7],4],[[7,8],[0,13]]],[1,1]]}")

# smallfish_number = [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
# split(smallfish_number)
# print(f"{smallfish_number == [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]} {smallfish_number} == {[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]}")
# l1 = [[[[4,3],4],4],[7,[[8,4],9]]]
# l2 = [1,1]
# total = addition(l1, l2)
# print(f"{total == [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]}")
# reduce(total)
# print(f"{total == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]}")


