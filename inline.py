for i in range(1,11):
  print('{:<3}|'.format(i),end= "")
  #:<3 = three left shift 
  for j in range(1,11):
    print('{:>4}|'.format(i*j),end= "")
  if i==1:
    print('\n{:#^40}'.format(),end="")
  print("")  