x = input('Enter the number: ')
ln = len(x)
j = ln-1
while True:
    for i in x[j]:
        if j < 0:
            break
        print(i, end=' ')
        j = j - 1

#OR
#x = input('Enter the number: ')
#for i in x[::-1]:
#    print(i, end=' ')