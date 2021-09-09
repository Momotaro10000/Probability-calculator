import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for ball, num in kwargs.items():
      self.contents += num * [ball]

  def draw(self, num_balls_drawn):
    try:
      drawn = random.sample(self.contents, num_balls_drawn)
    except ValueError:
      drawn = copy.deepcopy(self.contents)

    for ball in drawn:
      self.contents.remove(ball)
    
    return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    draw_attempt = hat_copy.draw(num_balls_drawn)
    
    expected_result = []
    for ball, num in expected_balls.items():
      expected_result += num * [ball]

    if balls_in(expected_result, draw_attempt):
      M += 1

  return M / num_experiments

def balls_in(expected_balls, balls_drawn):
  # Check if expected amount of balls has been drawn
  for ball in expected_balls:
    if ball in balls_drawn:
      balls_drawn.remove(ball)
    else:
      return False
  return True

