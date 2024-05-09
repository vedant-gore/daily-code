#FUNCTION CALLING
print('1st program:')
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
        
greet('en')
greet('es')
greet('fr')

#PROGRAM 2:
print('2nd program:')
def greet_ppl():
    return 'Hello'

print(greet_ppl(), 'Glenn')
print(greet_ppl(), 'Sally')

#PROGRAM 3:
print('3rd program:')
def addn(a,b):
    add = a+b
    return add

x = addn(3,5)
print(x)
