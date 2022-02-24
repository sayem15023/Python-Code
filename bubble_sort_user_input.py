def bubblesort(a,number):
  for i in range(number-1):
    for j in range(number-i-1):
      if(a[j]>a[j+1]):
        a[j],a[j+1]=a[j+1],a[j]
a = []
number = int(input("Enter the total number of element"))
for i in range(number):
  value = int(input("enter the element"%i))
  a.append(value)
bubblesort(a,number)
print("The sorted list in assending order",a)