class car:
  
  def __init__(self):
    self.__updatesoftware()#private method
  def drive(self):
    print("driving")
  def __updatesoftware(self):
    print("updating software")
blackcar =car()
blackcar.drive()     