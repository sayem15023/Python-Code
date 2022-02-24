num = int(input("How many numbers you enter:"))
list1 = [int(input("Enter the numbers"))for x in range(num)]
print(list1)
for j in range(len(list1)-1):
  #for more efficient we use how many times it works 
  #for i in range(len(list1)-1-j):
  for i in range(len(list1)-1):
    if list1[i]>list1[i+1]:
      list1[i],list1[i+1] = list1[i+1],list1[i]
print("sorted",list1)