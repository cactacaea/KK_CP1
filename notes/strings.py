# KK 2nd Strings Notes

# dictionaries
my_dictionary = {"name": "kris",
                 "age": "99",
                 "class": "CS",}
print(my_dictionary['age'])
# strings & examples
"content of string"
'content of string'

"The quick brown fox jumps over the lazy dog!" 
# cannot access this string since it's not stored in a varible ^
sentence = "The quick brown fox jumps over the lazy dog!" 
first_name = 'Xavier'
last_name = "LaRose"
month = 'September'
food = "ramen"
# if " or ' is needed 
name = "La'Rose"
best = '"The Return of the King" is the best book ever!'

funny = "The dog jumped into the lake"
# string length
length = len(month)
print(f"September has{length} letters!")
# escape characters
print('\tWill said \ndon\'t die')
# concatenation
full_name = first_name + " " + last_name
print(name)
# slicing strings
# string[start index, end index]
print(last_name[2:5])