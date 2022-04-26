"""
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself.
This has the benefit of meaning that you can loop through data to reach a result.

this can result in a stack overflow if care isn't taken
Recursion is more efficient than iteration
it requires more space than iteration too (downside)
-----------------------------------

Fibonacci Sequence
---------------
"""

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(11))


'''using iteration (using a constant space and not waste memory) '''
def fib2(n):
    if n == 0 or n == 1:
        return n

    s_last = 0
    last = 1
    curr_pos = 2

    while curr_pos <= n:
        temp = last
        last = last + s_last
        s_last = temp
        curr_pos += 1

    return last

print(fib2(11))