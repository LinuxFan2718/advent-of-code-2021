import sys
DEBUG = True
position = [None, 4, 8]
score = [None, 0, 0]
rolls = 0

dice_sides = 100
def dice_roll():
  roll = 1
  while True:
    yield roll
    roll += 1
    if roll > 100:
      roll = 1

die = dice_roll()

def report():
  for i in [1,2]:
    print(f"player {i} position {position[i]} score {score[i]} score*rolls = {score[i]*rolls}")
  print(f"rolls {rolls}")
  sys.exit()

def turn(player):
  global rolls
  rolls += 3

  roll = [next(die), next(die), next(die)]
  if DEBUG:
    print(f"player {player} rolls {roll}")
  result = sum(roll)
  adjusted_result = result % 10
  current_position = position[player]
  current_position += adjusted_result
  if current_position > 10:
    current_position -= 10
  position[player] = current_position
  if DEBUG:
    print(f"player {player} current position {current_position}")
  score[player] += current_position
  if DEBUG:
    print(f"player {player} current score {score[player]}")
  if score[player] >= 1000:
    print(f"GAME OVER player {player} won with score {score[player]}")
    report()
  
while True:
  turn(1)
  turn(2)
