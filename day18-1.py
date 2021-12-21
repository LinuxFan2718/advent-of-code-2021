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
  while True:
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
      break

def split(smallfish_number):
  stop = False

  for i in range(len(smallfish_number)):
    if not stop and isinstance(smallfish_number[i], int):
      if smallfish_number[i] >= 10:
        stop = True
        if smallfish_number[i] % 2 == 0:
          newpair = [smallfish_number[i] // 2, smallfish_number[i] // 2]
        else:
          newpair = [smallfish_number[i] // 2, 1 + smallfish_number[i] // 2]
        smallfish_number[i] = newpair
        break
    elif not stop and isinstance(smallfish_number[i], list):
      for j in range(len(smallfish_number[i])):
        if not stop and isinstance(smallfish_number[i][j], int):
          if smallfish_number[i][j] >= 10:
            stop = True
            if smallfish_number[i][j] % 2 == 0:
              newpair = [smallfish_number[i][j] // 2, smallfish_number[i][j] // 2]
            else:
              newpair = [smallfish_number[i][j] // 2, 1 + smallfish_number[i][j] // 2]
            smallfish_number[i][j] = newpair
            break 
        elif not stop and isinstance(smallfish_number[i][j], list):
          for k in range(len(smallfish_number[i][j])):
            if not stop and isinstance(smallfish_number[i][j][k], int):
              if smallfish_number[i][j][k] >= 10:
                stop = True
                if smallfish_number[i][j][k] % 2 == 0:
                  newpair = [smallfish_number[i][j][k] // 2, smallfish_number[i][j][k] // 2]
                else:
                  newpair = [smallfish_number[i][j][k] // 2, 1 + smallfish_number[i][j][k] // 2]
                smallfish_number[i][j][k] = newpair
                break
            elif not stop and isinstance(smallfish_number[i][j][k], list):
              for m in range(len(smallfish_number[i][j][k])):
                element = smallfish_number[i][j][k][m]
                if not stop and isinstance(element, int):
                  if element >= 10:
                    stop = True
                    if element % 2 == 0:
                      newpair = [element // 2, element // 2]
                    else:
                      newpair = [element // 2, 1 + element // 2]
                    smallfish_number[i][j][k][m] = newpair
                    break
                  
                if isinstance(element, list):
                  print(f"should not happen {element} is a list {i} {j} {k} {m}")
  return stop

def magnitude(smallfish_number):
  if isinstance(smallfish_number, int):
    return smallfish_number
  elif isinstance(smallfish_number, list):
    return 3 * magnitude(smallfish_number[0]) + 2 * magnitude(smallfish_number[1])

def addition(smallfish_number1, smallfish_number2):
  ans = [smallfish_number1, smallfish_number2]

  return ans
  
def reduce(smallfish_number):
  did_split = False
  did_explode = explode(smallfish_number)
  if not did_explode:
    did_split = split(smallfish_number)
  if did_explode or did_split:
    reduce(smallfish_number)
  return None

# filename = 'input18-test2.txt'
# f = open(filename)
# snailfish_numbers = []
# while True:
#   line = f.readline().strip()
#   if line == '':
#     break
#   snailfish_numbers.append(eval(line))
# snailfish_numbers = [
#   [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],
#   [7,[[[3,7],[4,3]],[[6,3],[8,8]]]],
#   [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]],
#   [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]],
#   [7,[5,[[3,8],[1,4]]]],
#   [[2,[2,2]],[8,[8,1]]],
#   [2,9],
#   [1,[[[9,3],9],[[9,0],[0,7]]]],
#   [[[5,[7,4]],7],1],
#   [[[[4,2],2],6],[8,7]]
# ]

# running_sum = snailfish_numbers[0]
# for x in range(1, len(snailfish_numbers)):
#   print(f"  {running_sum}")
#   print(f"+ {snailfish_numbers[x]}")
#   running_sum = addition(running_sum[:], snailfish_numbers[x])
#   reduce(running_sum)
#   print(f"= {running_sum}")
#   print()
#   pass

l1 = [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]
l2 = [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]]
l3 = addition(l1, l2)
reduce(l3)
print(f"{l3}")

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


