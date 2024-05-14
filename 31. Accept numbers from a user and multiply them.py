i = 0
lst = list()
while i < 2:
    inp = input('Enter a number:')
    inp = int(inp)
    lst.append(inp)
    i = i + 1
print('The two numbers are:', lst)

print('Their multiplication is:', lst[0]*lst[1])
