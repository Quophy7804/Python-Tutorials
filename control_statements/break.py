'''
The BREAK keyword is used to forcibly end a loop
let's take a look at an example
'''

for i in range(5):
    print("Hello World")
    if (i == 1):
        break

'''
since the loop starts from 0 index, I told the loop to stop when i gets to 1,
which is exactly what happened.
'''