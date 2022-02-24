month = [2200,2350,2600,2130,2190]
#find extra money
x = month[1] - month[0]
print("In February we spent extra" ,x, "dollars")
#find out total expense
y = month[0] + month[1]
z = y + month[2]
print("Total expense in first quarter is", z)
month.append(1979)
print("Expense at the end of the june is ",month)