'''like a list
a tuple in an ordered collection
however, tuples cannot be changed

indexing is also the same as in list positive and negative numbers
'''

collection = (1, 2, 3)
print(collection[0])

'''
A work around with tuples in changing vlaues is to convert the 
tuple to list, make the changes and convert it back to a tuple
'''

collection2 = list(collection)
collection2[0] = 4
collection = tuple(collection2)

print(collection)

# loop over a tuple, lets use a for loop
for i in collection:
    print(i)
# ------------ if statement------
if 2 in collection:
    print("2 is in the tuple")
else:
    print("2 is not in the tuple")

'''
Just like using the extend function the join list;
we'll concatenate using tuples
'''

collection3 = (4, 5, 6)
totCollection = collection + collection3
print(totCollection)

'''
COUNT
'''

print("The number 4 appears: ", totCollection.count(4), " times in the tuple")