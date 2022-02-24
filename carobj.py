class Car:
  def __init__(self,n,c):
    self.name = n
    self.color = c
  def start(self):
    print("name:",self.name)
    print("color",self.color)
    print("starting the engine")
my_car1 = Car("corolla","white")
my_car1.start()
my_car2 = Car("premio","Black")
my_car2.start()
my_car3 = Car("allion","blue")
my_car3.start()      