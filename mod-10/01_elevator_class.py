class Elevator:
  def __init__(self, min_floor, max_floor):
    self.min_floor = min_floor
    self.max_floor = max_floor
    self.current_floor = self.min_floor

  def go_to_floor(self, floor):
    go_down = False

    if floor < self.current_floor:
      go_down = True

    for _ in range(abs(self.current_floor - floor)):
      if go_down:
        self.floor_down()
      else:
        self.floor_up()

  def floor_up(self):
    if self.max_floor < self.current_floor + 1:
      return
    self.current_floor += 1
  def floor_down(self):
    if self.min_floor > self.current_floor - 1:
      return
    self.current_floor -= 1
