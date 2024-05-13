print('Print characters from a string that are present at an even index number')
x = input('original string is: ')
print('printing only even  index chars')
for i in x[0::2]:
    if i == ' ':
        continue
    print(i)
