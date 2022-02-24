daily_temps = {'sun':54,'mon':45,'tue':67,'wed':70,'thur':77,'fri':79,'sat':66}
dayname = {'sun':'sunday','mon':'Monday','tue':'tuesday','wed':'wednesday','thur':'thursday','fri':'friday','sat': 'saturday'}
day = input("enter 'sun','mon','tue','wed','thur','fri','sat'")
print("The temperature for",dayname[day],"was",daily_temps[day],"degree")