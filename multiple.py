class land_animal:
  def printing(self):
    print("this is land animal")
class water_animal:
  def display(self):
    print("this is water animal")
class frog(land_animal,water_animal):
  pass
p1 = frog()
p1.printing()
p1.display()