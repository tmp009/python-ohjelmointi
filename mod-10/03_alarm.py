class Elevator:
  def __init__(self, min_floor, max_floor):
    self.bottom_floor = min_floor
    self.top_floor = max_floor
    self.current_floor = self.bottom_floor

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
    if self.top_floor < self.current_floor + 1:
      return
    self.current_floor += 1
  def floor_down(self):
    if self.bottom_floor > self.current_floor - 1:
      return
    self.current_floor -= 1

class Building:
  def __init__(self, bottom_floor, top_floor, elevator_count):
    self.bottom_floor= bottom_floor
    self.top_floor = top_floor
    self.elevators = [ Elevator(bottom_floor, top_floor) for _ in range(elevator_count) ]

  def run_elevator(self, elevator, floor):
    self.elevators[elevator].go_to_floor(floor)

  def fire_alarm(self):
    for elevator in self.elevators:
      elevator.go_to_floor(elevator.bottom_floor)
