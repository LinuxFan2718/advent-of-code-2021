DEBUG = True

input = "target area: x=20..30, y=-10..-5"
#input = "target area: x=96..125, y=-144..-98"

sub_input = input[13:]
sub_input_x, sub_input_y = sub_input.split(', ')
xl, xr = [ int(n) for n in sub_input_x[2:].split('..')]
yb, yt = [ int(n) for n in sub_input_y[2:].split('..')]

x, y = 0, 0

def hit_target(x, y, xl, xr, yb, yt):
  return xl <= x and x <= xr and yb <= y and y <= yt

def missed_target(x, y, xr, yb, yt):
  if yv <= 0 and y < yb: # no upward velocity
    return True
  return False

xv, yv = 9, 0
initial = [xv, yv]
while True:
  x += xv
  if xv > 0:
    xv -= 1
  elif xv < 0:
    xv += 1
  y += yv
  yv -= 1
  if hit_target(x, y, xl, xr, yb, yt):
    if DEBUG:
      print(f"hit target x = {x} y = {y} initial velocity x, y = {initial}")
    break
  
  if missed_target(x, y, xr, yb, yv):
    if DEBUG:
      print(f"miss target final position x = {x} y = {y} initial velocity x, y = {initial}")
    break
  if DEBUG:
    print(f"x = {x} y = {y}")

print(f"simulation completed")