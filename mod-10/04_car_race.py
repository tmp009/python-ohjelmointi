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

class Race:
  def __init__(self, name, distance, cars: list[Car]):
    self.name = name
    self.distance = distance
    self.cars = cars
    self.race_is_active = len(cars) > 0

  def print_status(self):
    print(f"{'License Plate':<12} {'Max Speed':>9} {'Current Speed':>14} {'Distance':>10}")
    print("-" * 50)
    for car in self.cars:
      print(f"{car.license_plate:<12} {car.maximum_speed:>9} {car.current_speed:>14} {car.travelled_distance:>10.1f}")

  def race_finished(self):
    is_finished = False
    for car in self.cars:
      is_over_distance = car.travelled_distance > self.distance

      if is_over_distance:
        is_finished = True
        break
    return is_finished

  def hour_passes(self):
    for car in self.cars:
      accelerate_speed = random.randint(-10, 15)
      car.accelerate(accelerate_speed)
      car.drive(1)


    return self.cars
