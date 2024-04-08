# Split a string without removing the delimiter in Python

my_str = 'bobby_hadz_com'

delimiter = '_'

my_list = [x+delimiter for x in my_str.split(delimiter) if x]

# 👇️ ['bobby_', 'hadz_', 'com_']
print(my_list)