class A:
  def display(self):
    print("method belongs to class A")
class B(A):
  def display(self):
    print("method belongs to class B")
s = B()
s.display()