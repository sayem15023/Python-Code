stack = []
def push():
  if len (stack)==n:
    print("List is full")
  element = input("Enter the element")
  stack.append(element)
  print(stack)
def pop():
  if not stack:
    print("Stack is empty")
  else:
    element = stack.pop()
    print("Remove element",element)
    print(stack)
#limit of the stack
n = int(input("LIMIT of stack"))
while True:
  print("select the operation 1.push 2,pop 3.quit")
  choice = int(input())
  if choice==1:
    push()
  elif choice==2:
    pop()
  elif choice==3:
    break
  else:
    print("ENTER the correct operation")