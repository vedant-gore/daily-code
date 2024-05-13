numlist = list()
while True:
    inp = input('Enter a number:')
    if inp == 'done':
        break
    inp = int(inp)
    numlist.append(inp)

print('The list is: ', numlist)
#x = len(numlist)
#if numlist[0] == numlist[x-1]:
if numlist[0] == numlist[-1]:
    print('result is true')
else:
    print('Result is false')