filename = 'input4.txt'
numbers = []
f = open(filename)
raw_numbers = f.readline()
nums = [int(x) for x in raw_numbers.strip().split(',')]

boards = []
while True:
  empty_line = f.readline()
  if empty_line == '':
    break
  board = []
  for i in range(5):
    row = [int(x) for x in f.readline().strip().split()]
    board.append(row)
  boards.append(board)

def winner(nums, i, board):
  for row in board:
    if all([x in nums[0:i] for x in row]):
      return True
  for j in range(5):
    column = [row[j] for row in board]
    if all([x in nums[0:i] for x in column]):
      return True
  return False

i = 5
won = False
while won == False and i < len(nums):
  for board in boards:
    if winner(nums, i, board):
      won = True
      sum_unmarked_nums = sum([x for row in board for x in row if x not in nums[0:i]])
      num_just_called = nums[i-1]
      final_score = sum_unmarked_nums * num_just_called
      print(f"final score = {final_score}")
      break
  i += 1

