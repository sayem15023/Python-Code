#only for non duplicate number
#list1 = [56,3,2,76,6,0]
#for duplicate we use
list1 = [3,5,45,3,67]
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
#for max it use max