from abc import ABC,abstractmethod
class Shape(ABC):
  def __init__(self,d1,d2):
    self.d1 = d1
    self.d2 = d2
  def area(self):
    pass
