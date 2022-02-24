def bubble_sort(list1):
  for i in range(0,len(list1)-1):#outer loop
    for j in range(len(list1)-1):#inner loop
      if(list1[j]>list1[j+1]):
        list1[j],list1[j+1] = list1[j+1],list1[j]
  return list1
list1 =[5,3,9,7,2]
print("The unsorted list is:",list1)
print("The sorted list is:",bubble_sort(list1))
