def search(list1,key):
  for i in range(len(list1)):
    if key == list1[i]:
      print("key element is found")
      break
  else:
    print("element is not found")

#num = int(input("list length"))
#list1 = [int(input()) for i in range(num)]
list1 = [34,4,5,6,23,15]
key = int(input("enter the key element"))
search(list1,key)
