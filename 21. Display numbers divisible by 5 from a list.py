numlist = list()
while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    x = int(x)
    numlist.append(x)

print('The list is: ', numlist)
for i in numlist:
    if i % 5 != 0:
        continue
    print(i)
