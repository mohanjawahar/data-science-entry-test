# Class instance
class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def describe_car(self):
    print(f'Car Make: {self.make} , Car Model: {self.model} , Car Make Year: {self.year}')

# Instance of the Car class with attributes
car1 = Car(make='Toyota',model='Corolla',year=2020)

# call the car function to print the instance
car1.describe_car()
