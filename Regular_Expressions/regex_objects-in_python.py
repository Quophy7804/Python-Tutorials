import re

text = "Happy happy birthday"
result = re.search("^Happy.*birthday$", text)
print(result)