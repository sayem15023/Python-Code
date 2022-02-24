#write in a file 
text = open("text.txt","w")
text.write("hello people")
text.close()
#append something in a file
text = open("text.txt","a")
text.write(" welcome to jungle")
text.close()
#read a file
text = open("text.txt",'r')
print(text.read())
text.close()