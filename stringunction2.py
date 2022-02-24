#find function
s = "Hello world"
print(s.find('d'))
print(s.find('world'))
#split function
print(s.split())
print(s.split('o'))
#lower
print(s.lower())
#upper
print(s.upper())
#swapcase convert uppercase to lower case lower to upper
print(s.swapcase())
#replace function
print(s.replace('world','everyone'))
#remove extra caracter from left side to right side not in middle, string using strip
s1 = "????? hello??"
print(s1.strip('?'))
#lstrip
print(s1.lstrip('?'))
print(s1.rstrip('?'))