class Vehicle:
  def __init__(self,name,manufacturer,color):
    self.name = name
    self.manufacturer = manufacturer
    self.color = color
  def turn(self,direction):
    print("turning",self.name,"to",direction)
class Car(Vehicle):
  def __init__(self,name,manufacturer,color,year):
    self.name = name
    self.manufacturer = manufacturer
    self.color = color
    self.year = 2022
  def change_gear(self,gear_name):
    print(self.name,"is changing gear to",gear_name)
  def turn(self,direction):
    print("self.name","is turning",direction)
if __name__ == "__main__":
  c = Car("mustang","Ford","Red",2022)
  v = Vehicle("softail delux","Harley-davidson","Blue")
c.turn("right")
v.turn("right")
