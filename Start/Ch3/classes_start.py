# Example file for working with classes
# a class is a way to encapsulate functionalities and data that can be kept together and
# reuse as a module in another projects

#create a base class Vehicle
class Vehicle:
  #special function __init__() as a constructor
  def __init__(self, bodyStyle):
    self.bodyStyle = bodyStyle

  #define a behavior
  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

#create a subclass called Car that inherits from base class Vehicle
class Car(Vehicle):
  def __init__(self, engineType):
    super().__init__("Car") # setting the bodyStyle property of the super class, 'self' param is taking care of auto by python
    self.engine = engineType
    self.wheels = 4
    self.doors = 4
  #override the bahavior drive
  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engine, "Car at", self.speed)

# subclass Motorcycle
class Motorcycle(Vehicle):
  def __init__(self, engineType, hasSideCar):
    super().__init__("Motorcycle")
    if hasSideCar:
      self.wheels = 3
    else:
      self.wheels = 2

    self.doors = 0
    self.engine = engineType

  #override the bahavior drive
  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engine, "Motorcycle at", self.speed)

#create objects
car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

# accessing obj values
print(f"mc1 has {mc1.wheels} wheels")
print("car1 num of doors are",car1.doors)
print("car2 engine type is", car2.engine)
car1.drive(30)
car2.drive(40)
mc1.drive(50)

