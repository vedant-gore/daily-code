#PYTHON EXERCISES FOR BEGINNERS
print('Program 1: Calculate the multiplication and sum of two numbers:')
def func(a,b):
    if a*b <= 1000:
        return a*b
    else:
        return a+b

x = (input('Enter first number: '))
num1 = int(x)
y = (input('Enter second number:'))
num2 = int(y)
print('The result is:', func(num1,num2))