'''
A Set:

is an unordered collection of elements that donnot contain any duplicates

The set is inside a curly braces
'''

collection = {"a", "b", "c"}

# adding to the set
"""
collection.add("d")

print(collection)

''' Removing from the set, use the discard function '''
collection.discard("a")

print("removing 'a': ",collection )

'''
here the POP function is used to remove a random item from the set
'''

collection.pop()
print("using pop: ",collection)
"""
# finding the difference between sets

collection2 = {"d", "e", "c"}

print("difference: ", collection.difference(collection2))

''' Intersection '''
print("intersection: ", collection.intersection(collection2))

''' Union/combining sets '''
print("Union: ", collection.union(collection2))

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
subsets & supersets
'''
print()

collection3 = {"a", "b"}
print("subset: ", collection3.issubset(collection))
print()
print("superset: ", collection3.issuperset(collection))
