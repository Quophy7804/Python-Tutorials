'''
There are 5 data types
-----------------------

String(str): text
Integer(int): positive and negative numbers and zero
Floating point: decimals
Booleans: True or False
list (called array in other languages)

Character: not used in python
'''

'''str
text = "The quick brown fox jumped over the lazy dog"
t1 = "dog" in text
print(t1)

'''

'''int
int1 = 3
int2 = 2
print(int1 + int2)

works with +, -, *, / and //
'''

'''floating point
works just like the integers but with the decimal points twist.
Here, nothing is lost even if its .01

x = 3.5
y = 2.1
print(x + y)
'''

'''Booleans
bool1 = True
bool2 = False

only zero passes as false and the booleans are stated with a capital 'T' and 'F'
print(bool(-1)) will also give a True bool.

an empty collection will also pass a false value
print(bool(1))

print(bool([]))
'''


'''List
A list is an ordered collection of data.
They're the python equivalent of arrays
'''
collection = [1, 2, 3]

print(len(collection)) # want to see how many elements there are in the list

# indexing
print("the number at this index is: ", collection[0])

''' we can change a value in the list'''
collection[2] = 5

print("The new values after one has been changed: ", collection)

for i in range(len(collection)): # iterating over the list
    print(collection[i])

'''checking of the list has a specified item
if 1 in collection:
    print("1 is in the list")
else:
    print("1 is not in the list")
'''

collection.append(7) # Append function is used to add elements to the list
print(collection)

# delete/clear the list
collection.clear()
print("taadaaaaaa, I'm empty now", collection)

'''sorting function'''
collection1 = [2, 3, 1]
collection1.sort()
print(collection1)

collection1.reverse() # I guess you know what this will do

print(collection1.count(2)) # this counts the number of times 2 appeared/instanced in the list

''' combing 2 diff list '''
new = [1, 2, 3]
new1 = [4, 5, 6]

new.extend(new1)
print(new) # this adds the list in the extend function to the previous

print (new.index(2)) # finding the index on the element 2

''' insert function inserts into the list without deleting any but does so with the index '''
new.insert(0, 9)
print(new)

# pop and remove
new.pop(0) #uses the index
print('using pop: ', new)
new.remove(4) #uses the element, itself
print("using remove: ", new)