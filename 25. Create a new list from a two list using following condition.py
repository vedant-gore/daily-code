numlist1 = list()
while True:
    x = input('Enter the number: ')
    if x == 'done':
        break
    x = int(x)
    numlist1.append(x)

numlist2 = list()
while True:
    y = input('Enter the number: ')
    if y == 'done':
        break
    y = int(y)
    numlist2.append(y)

print('list 1 is', numlist1)
print('list 2 is', numlist2)

numlist3 = list()
for i in numlist1:
    if i % 2 == 0:
        continue
    a = i
    numlist3.append(a)

for j in numlist2:
    if j % 2 == 0:
        b = j
        numlist3.append(b)
    else:
        continue

print('result list:',numlist3)