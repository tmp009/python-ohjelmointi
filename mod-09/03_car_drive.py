class Car:
  def __init__(self, license_plate, maximum_speed):
    self.license_plate = license_plate
    self.maximum_speed = maximum_speed
    self.current_speed = 0
    self.travelled_distance = 0

  def accelerate(self, change):
    new_speed = self.current_speed + change

    if new_speed > self.maximum_speed or new_speed < 0:
      self.current_speed = 0
    else:
      self.current_speed = new_speed

  def drive(self, hours):
    self.travelled_distance += self.current_speed * hours
