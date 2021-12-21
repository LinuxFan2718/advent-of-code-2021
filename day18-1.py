filename = 'input18-test.txt'
f = open(filename)
snailfish_numbers = []
while True:
  line = f.readline().strip()
  if line == '':
    break
  snailfish_numbers.append(eval(line))

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
                if isinstance(element, list):
                  nested_in_four = temp

  if nested_in_four == None:
    return None

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
    if 'm' in int_to_the_right:
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


def magnitude(smallfish_number):
  return None

def split(smallfish_number):
  return None

def addition(smallfish_number1, smallfish_number2):
  ans = [smallfish_number1, smallfish_number2]

  return ans
  
def reduce(smallfish_number):
  return None

smallfish_number = [[[[[9,8],1],2],3],4]
explode(smallfish_number)
print(f"{smallfish_number == [[[[0,9],2],3],4]}  {smallfish_number} == {[[[[0, 9], 2], 3], 4]}")

smallfish_number = [7,[6,[5,[4,[3,2]]]]]
explode(smallfish_number)
print(f"{smallfish_number == [7,[6,[5,[7,0]]]]}")

smallfish_number = [[6,[5,[4,[3,2]]]],1]
explode(smallfish_number)
print(f"{smallfish_number == [[6,[5,[7,0]]],3]} {smallfish_number} == [[6, [5, [7, 0]]], 3]")


smallfish_number = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
explode(smallfish_number)
print(f"{smallfish_number == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]}")

smallfish_number = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
explode(smallfish_number)
print(f"{smallfish_number == [[3,[2,[8,0]]],[9,[5,[7,0]]]]}")
