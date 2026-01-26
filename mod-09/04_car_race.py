import random

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

def race(cars: list[Car]):
  race_is_active = True

  while race_is_active:
    for car in cars:
      accelerate_speed = random.randint(-10, 15)
      car.accelerate(accelerate_speed)
      car.drive(1)

      is_over_10000km = car.travelled_distance >= 10_000

      if is_over_10000km:
        race_is_active = False
        break


  return cars
