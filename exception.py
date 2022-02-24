import math
num = int(input("Please enter the number to calculate factorial"))
#result = math.factorial(num)
#print(result)
#try and except blog
try:
  result = math.factorial(num)
  print(result)
except:
  print("cannot compute the factorial of negative numbers")