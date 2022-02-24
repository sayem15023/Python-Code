#rising exception force exception to occure
try:
  #num = int(input("Enter the number "))
 
 #  if num<=0:
    raise ValueError("that is not positive number")
except ValueError as error:
  print(error)
  #finally clause is executed
  import math
  num = int(input("input"))
  try:
    result = math.factorial(num)
    print(result)
  finally:
    print("goodby")