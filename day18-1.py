filename = 'input18-test.txt'
f = open(filename)
snailfish_numbers = []
while True:
  line = f.readline().strip()
  if line == '':
    break
  snailfish_numbers.append(eval(line))

def magnitude(smallfish_number):
  return None

def split(smallfish_number):
  return None

def explode(smallfish_number):
  # find leftmost pair nested inside four pairs
  nested_in_four = []

  for i in range(len(smallfish_number)):
    if isinstance(smallfish_number[i], list):
      for j in range(len(smallfish_number[i])):
        if isinstance(smallfish_number[i][j], list):
          for k in range(len(smallfish_number[i][j])):
            if isinstance(smallfish_number[i][j][k], list):
              for m in range(len(smallfish_number[i][j][k])):
                if isinstance(smallfish_number[i][j][k][m], list):
                  temp = {'i': i, 'j': j, 'k': k, 'm': m }
                  nested_in_four.append(temp)
  # if none, do nothing
  if nested_in_four == []:
    return None
  # if there is one, remove it
  i, j, k, m = nested_in_four[0]['i'], nested_in_four[0]['j'], nested_in_four[0]['k'], nested_in_four[0]['m']
  left, right = smallfish_number[i][j][k][m]
  smallfish_number[i][j][k][m] = 0
  # the pair's left value is added to the first regular number to the left of the exploding pair (if any)
  # first check the array that exploding pair came from
  added_left = False
  for mm in range(m-1, -1, -1):
    if not added_left and isinstance(smallfish_number[i][j][k][mm], int):
      smallfish_number[i][j][k][mm] += left
      added_left = True
      break

  if not added_left:
    for ii in range(i, -1, -1): # inclusive i and 0
      for jj in range(j, -1, -1):
        for kk in range(k, -1, -1):
          for mm in range(len(smallfish_number[ii][jj][kk])-1, -1, -1):
            if not added_left and isinstance(smallfish_number[ii][jj][kk][mm], int):
              smallfish_number[ii][jj][kk][mm] += left
              added_left = True
              break

  # the pair's right value is added to the first regular number to the right of the exploding pair (if any)

  return nested_in_four

def addition(smallfish_number1, smallfish_number2):
  ans = [smallfish_number1, smallfish_number2]

  return ans

  
def reduce(smallfish_number):
  return None

smallfish_number = [[[[[9,8],1],2],3],4]
smallfish_number = [7,[6,[5,[4,[3,2]]]]]
smallfish_number = [[6,[5,[4,[3,2]]]],1]
smallfish_number = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
smallfish_number = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
res = explode(smallfish_number)
pass