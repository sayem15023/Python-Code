#using list
daily_temps = [67,72,79,65,62,56,75]
day = input("enter 'sun','mon','tue','wed','thur','fri','sat'")
if day == 'sun':
  dayname = 'Sunday'
  temp = daily_temps[0]
elif day =='mon':
  dayname = 'Monday'
  temp = daily_temps[1]
elif day == 'tue':
  dayname = 'Tuesday'
  temp = daily_temps[2]
elif day =='wed':
  dayname = 'Wednesday'
  temp = daily_temps[3]
elif day =='thur':
  dayname = 'Thursday'
  temp = daily_temps[4]
elif day =='fri':
  dayname = 'Friday'
  temp = daily_temps[5]
elif day =='sat':
  dayname = 'Saturday'
  temp = daily_temps[6]
else:
  print("wrong input")
print("The Temperature for:",dayname,"was",temp,"degree")
  