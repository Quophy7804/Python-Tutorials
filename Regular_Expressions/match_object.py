"""
The match object is an object that contains information about the search and the result
"""

import re

text = "Happy happy birthday"
result = re.search("^Happy.*birthday$", text)
print(result.group())