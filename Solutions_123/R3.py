# Part Three author Edgar Allen 
name= 'Edgar Allen'
"""
Given an input text, Code a program (in python) that displays the number of
repetitions of each word.
Sample text: "Hi how are things? How are you? Are you a developer? I am also a
developer"
"""
symbol = '.,!¡?¿:' 

text = ''
memory = ''
words= []
compare = []
info = {}
def repeated_words(text):
    l_memory = text.lower()
    text = l_memory.translate(str.maketrans('', '', symbol))
    memory = text.split()
    #lower(memory)
    for i in memory:
        n = memory.count(i)
        r = i + ': '+str(n)+' '+'repetitions'
        if r not in words:
            words.append(r)
    #print (memory)
    #print (l_memory)
    #print (text, 'limpios')
    return words

text= str(input('Enter a text \n'))


print (f':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print (repeated_words (text)) 
print (f':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')


