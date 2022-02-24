class student:
  clg = 'xyz'#class variable
  def __init__(self,rollno,name):
    self.rollno = rollno
    self.name = name
  def display(self):
    print("student name:",self.name)
    print("student rollnumber:",self.rollno)
    print("college",self.clg)
s1 = student('15023','sayem')
s1.display()
s2 = student('15063','tipu')
s2.display()