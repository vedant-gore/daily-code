print('Print the sum of current and prev number')
pnum = 0
x = list(range(1, 11))
print(x)
for cnum in x:
    sum = pnum + cnum
    print('current num', cnum, 'prev num', pnum, 'sum:', sum)
    pnum = cnum
