# Part Two author Edgar Allen 
name= 'Edgar Allen'
"""
In mathematics, the Fibonacci sequence or serie is the following infinite 
sequence of natural numbers: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
1597 ... where f (0) = 0, f (1) = 1 and f (n) = f (n-1) + f (n-2).
Code a program (in python) that solves for any number in the Fibonacci series.
"""


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input('Get Number \n'))
print (f':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print (f'The number of the Fibonacci series is:{fibonacci(n)}')
print (f':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
