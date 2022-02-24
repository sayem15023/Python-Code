class animal:
  def eating(self):
    print("eating")
class dog(animal):#write down the base class name
  def bark(self):
    print("bark")
d = dog()
d.eating()#call the method eating
d.bark()#call the method bark