"""
example = "abc"
if example.startswith("a"):
    print("string starts with an a")


if example.endswith("c"):
    print("string ends with c")


'''' 
functions
-----------
.upper()
.lower()
.title() caps the first letters in each word
.capitalize() make the first letter caps
.find()    find the location/index
.count()   count the number of times items appears
.isupper() checking if the string/text are in upper case (returns a boolean)
.islower() checking if the string/text are in lower case (returns a boolean)
.isspace() checking for white space
.isnumeric() checking if the string contains digits (returns a boolean)
isdigit() same as above just that with this every element has to be a digit.
istitle() same as above, check if the string/text is title and returns a boolean.
'''

'''string formatting '''
price = 10
text = "The item cost {} dollars"

print(text.format(price))
"""

''' replacing '''

#text = "Happy Birthday!"

# print(text.replace("!", "s"))

''' join '''
example = ["a", "b", "c", "d"]
x = "-".join(example)
print(x)