import re

"""
Question:
----------
Find all occurances of l in the text
"""

def example():
    text = "Hello World"
    result = re.findall("[l]", text)
    print(result)