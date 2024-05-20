s = int(input('Enter start: '))
e = int(input('Enter end: '))
for num in range(s, e+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

