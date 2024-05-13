"""
first rs 10000 0% IR
next rs 10000 10% IR
remaining     20% IR
"""

inc = int(input('Enter your income: '))

if inc <= 10000:
    tax = 0
elif inc <= 20000:
    x = inc - 10000
    tax = x*10/100
else:
    tax = 0
    tax = 10000*10/100
    tax = tax + (inc - 20000)*20/100

print('Total payable tax is',tax)