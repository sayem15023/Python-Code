queue = []
def enqueue():
  element = input("Enter the element")
  queue.append(element)
  print(queue,"is added to queue")
def dequeue():
  if not queue:
    print("queue is empty")
  else:
    element = queue.pop(0)
    print("removed element")
def display():
  print(queue)
while True:
  print("select the operation 1.add 2.remove 3.show 4.quit")
  choice = int(input())
  if choice==1:
    enqueue()
  elif choice==2:
    dequeue()
  elif choice==3:
    display()
  elif choice==4:
    break
  else:
    print("Enter the correct opreation")
    