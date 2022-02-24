#using curly bracket syntex 
my_dict = {1:'apple',2:'ball',3:'cat'}
print(my_dict)
#creating empty dict,fill in the entries one by one
book = {}
book[1] = "apple"
book[2] = "ball"
book[3] = "dog"
print(book)
#dictionary constructor and a list of tuples
d = dict([(1,"rijr"),(2,"4rg")])#(all are tuples)
print(d)
#from two parallel list
a = [1,2,3,4]
b = ["apple","dog","cat","dehf"]
dol = {}
for i in range(len(a)):
  dol[a[i]] = b[i]
  print(dol)