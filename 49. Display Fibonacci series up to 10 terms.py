terms = int(input('Enter the number of terms: '))
num1 = 0
num2 = 1
sum = 0
for i in range(terms+1):
    print(num1, end=" ")
    sum = num1 + num2
    num1 = num2
    num2 = sum
