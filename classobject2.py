#class person:
  #def display(self):
 #   print("Hello")
#person1 = person()
#person1.display()
#init methods
class person:
  def __init__(self,name):
      self.name = name
  def display(self):
    print("Hello",self.name)
person1 =person ("Murgi")
person1.display()