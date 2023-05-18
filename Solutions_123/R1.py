# Part One author Edgar Allen 
name= 'Edgar Allen'
"""
    1. Code a program (in python) that displays the numbers from 1 to 100 
    on the screen, substituting the multiples of 3 for the word "fizz", 
    the multiples of 5 for "buzz" and the multiples of both, that is, 
    the multiples of 3 and 5, by the word "fizz buzz".
"""
print(f'Test Python Developer:{name}')
numbers = []
i = 0
position = ''
while i < 100:
    i= i+1
    numbers.append(i)
print ('numbers from 1 to 100')
print (numbers)
for i in numbers:
    if (i % 3 == 0):
        position = numbers.index(i)
        numbers[position]='fizz'
    elif (i % 5 == 0):
        position = numbers.index(i)
        numbers[position]='buzz'
    elif (i % 3 == 0) and (i % 5 == 0):
        position = numbers.index(i)
        numbers[position]='fizz buzz'
print (f':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print (numbers)
print (f':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    


#def Generatenumber():
