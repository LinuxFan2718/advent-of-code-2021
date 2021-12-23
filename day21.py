position = [None, 4, 8]
score = [None, 0, 0]

dice_sides = 100
def dice_roll():
   roll = 1
   while True:
       yield roll
       roll += 1
       if roll > 100:
         roll = 1

die = dice_roll()

for i in range(250):
  roll = next(die)
  print(roll)