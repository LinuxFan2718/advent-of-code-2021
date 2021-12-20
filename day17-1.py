DEBUG = True
VERBOSE = False

#input = "target area: x=20..30, y=-10..-5"
input = "target area: x=96..125, y=-144..-98"

sub_input = input[13:]
sub_input_x, sub_input_y = sub_input.split(', ')
xl, xr = [ int(n) for n in sub_input_x[2:].split('..')]
yb, yt = [ int(n) for n in sub_input_y[2:].split('..')]

def hit_target(x, y, xl, xr, yb, yt):
  return xl <= x and x <= xr and yb <= y and y <= yt

def missed_target(x, y, xr, yb, yt):
  if yv <= 0 and y < yb: # no upward velocity
    return True
  return False

#xv, yv = 15, 0
meta_highest_y = 0
meta_initial = None
for start_xv in range(20):
  if VERBOSE:
    print(f"x velocity = {start_xv}")
  for start_yv in range(100, 400):
    x, y = 0, 0
    initial = [start_xv, start_yv]
    highest_y = y
    xv, yv = start_xv, start_yv
    while True:
      x += xv
      if xv > 0:
        xv -= 1
      elif xv < 0:
        xv += 1
      y += yv
      yv -= 1
      if y > highest_y:
        highest_y = y

      if hit_target(x, y, xl, xr, yb, yt):
        if highest_y > meta_highest_y:
          meta_highest_y = highest_y
          meta_initial = initial
        if DEBUG:
          print(f"hit target x = {x} y = {y} initial velocity x, y = {initial} final v = {xv},{yv} highest y = {highest_y}")
        break
      
      if missed_target(x, y, xr, yb, yv):
        if VERBOSE:
          print(f"miss target final position x = {x} y = {y} initial velocity x, y = {initial}")
        break
      if VERBOSE:
        print(f"x = {x} y = {y}")

print(f"simulation completed. Highest y = {meta_highest_y} with initial x, y = {meta_initial}")