from abc import ABC,abstractmethod
class abs(ABC):
 def print (self,x):
  print("passed value =" , x)
 @abstractmethod
 def test(self):
  print("we are inside abc")
class sub (abs):
 def test(self):
  print ("we are inside test")
test = sub()
test.test()
test.print(100)

