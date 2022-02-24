num = int(input("How many numbers you want to enter"))
list1 = [int(input("Enter the numbers:"))for x in range(num)]
print(list1)
#one itteration itself don't necessary cause that was last element
#for i in range(len(list1)-1):
for i in range(len(list1)):
  min_val = min(list1[i:])
  #for duplicate value we use 
  min_ind = list1.index(min_val,i)
  #min_ind = list1.index(min_val)
  list1[i],list1[min_ind] = list1[min_ind],list1[i]
print(list1)