def explode(smallfish_number):
  # find leftmost pair nested inside four pairs
  nested_in_four = None
  int_to_the_left = None
  int_to_the_right = None
  stop_search = False

  # while iterating, keep track of
  # int that you would add to
  for i in range(len(smallfish_number)):
    if not stop_search and isinstance(smallfish_number[i], int):
      temp = {'i': i}
      if nested_in_four == None:
        int_to_the_left = temp
      elif nested_in_four:
        int_to_the_right = temp
        stop_search = True
        break
    elif not stop_search and isinstance(smallfish_number[i], list):
      for j in range(len(smallfish_number[i])):
        if not stop_search and isinstance(smallfish_number[i][j], int):
          temp = {'i': i, 'j': j}
          if nested_in_four == None:
            int_to_the_left = temp
          elif nested_in_four:
            int_to_the_right = temp
            stop_search = True
            break
        elif not stop_search and isinstance(smallfish_number[i][j], list):
          for k in range(len(smallfish_number[i][j])):
            if not stop_search and isinstance(smallfish_number[i][j][k], int):
              temp = {'i': i, 'j': j, 'k': k}
              if nested_in_four == None:
                int_to_the_left = temp
              elif nested_in_four:
                int_to_the_right = temp
                stop_search = True
                break
            elif not stop_search and isinstance(smallfish_number[i][j][k], list):
              for m in range(len(smallfish_number[i][j][k])):
                element = smallfish_number[i][j][k][m]
                temp = {'i': i, 'j': j, 'k': k, 'm': m }
                if isinstance(element, int):
                  if nested_in_four == None:
                    int_to_the_left = temp
                  elif nested_in_four:
                    int_to_the_right = temp
                    stop_search = True
                    break
                if not stop_search and isinstance(element, list):
                  if nested_in_four == None:
                    nested_in_four = temp
                  else:
                    int_to_the_right = {'i': i, 'j': j, 'k': k, 'm': m , 'n': 0}
                    stop_search = True


  if nested_in_four == None:
    return False

  # if there is one extract its values and change it to a 0 int
  i, j, k, m = nested_in_four['i'], nested_in_four['j'], nested_in_four['k'], nested_in_four['m']
  left, right = smallfish_number[i][j][k][m]
  smallfish_number[i][j][k][m] = 0
  # the pair's left value is added to the first regular number to the left of the exploding pair (if any)
  if int_to_the_left != None:
    if 'm' in int_to_the_left:
      i, j, k, m = int_to_the_left['i'], int_to_the_left['j'], int_to_the_left['k'], int_to_the_left['m']
      smallfish_number[i][j][k][m] += left
    elif 'k' in int_to_the_left:
      i, j, k = int_to_the_left['i'], int_to_the_left['j'], int_to_the_left['k']
      smallfish_number[i][j][k] += left
    elif 'j' in int_to_the_left:
      i, j = int_to_the_left['i'], int_to_the_left['j']
      smallfish_number[i][j] += left
    elif 'i' in int_to_the_left:
      i = int_to_the_left['i']
      smallfish_number[i] += left
  # the pair's right value is added to the first regular number to the right of the exploding pair (if any)
  if int_to_the_right != None:
    if 'n' in int_to_the_right:
      i, j, k, m = int_to_the_right['i'], int_to_the_right['j'], int_to_the_right['k'], int_to_the_right['m']
      smallfish_number[i][j][k][m][0] += right      
    elif 'm' in int_to_the_right:
      i, j, k, m = int_to_the_right['i'], int_to_the_right['j'], int_to_the_right['k'], int_to_the_right['m']
      smallfish_number[i][j][k][m] += right
    elif 'k' in int_to_the_right:
      i, j, k = int_to_the_right['i'], int_to_the_right['j'], int_to_the_right['k']
      smallfish_number[i][j][k] += right
    elif 'j' in int_to_the_right:
      i, j = int_to_the_right['i'], int_to_the_right['j']
      smallfish_number[i][j] += right
    elif 'i' in int_to_the_right:
      i = int_to_the_right['i']
      smallfish_number[i] += right
  return True

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
snailfish_numbers = [
  [1,1],
  [2,2],
  [3,3],
  [4,4],
  [5,5]
]

running_sum = snailfish_numbers[0]
for x in range(1, len(snailfish_numbers)):
  running_sum = addition(running_sum, snailfish_numbers[x])
  reduce(running_sum)

print(f"{running_sum}")

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


