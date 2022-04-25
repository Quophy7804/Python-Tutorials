'''
Dictionaries
----------------
It is a collection of key-value pairs (they are unordered)
'''

collection = dict()

# adding vlaues
collection["key1"] = "value1"
collection["key2"] = "value2"
collection["key3"] = "value3"

''' another way to create the dictionaries '''

collection2 = {"key1": "value1", "key2": "value2", "key3": "value3"}

''' dictionaries relies on hashing for finding items in it '''

''' we use the get function to retrieve values and the clear to clear as usual '''
print(collection2.get("key1"))


''' removing a key-value pair, use pop'''
#collection2.pop("key1")
#print(collection2)

''' looping '''
for i in collection2.keys():
    print(i)