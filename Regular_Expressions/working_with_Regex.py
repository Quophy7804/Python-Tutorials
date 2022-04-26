import re

text = "Hello World"
result = re.sub("\s", "-" , text)
print(result)

"""
re.split()
re.findall("[l,o]", text)
re.search("[l,o]", text)
"""