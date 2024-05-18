list1 = [10, 20, 30, 40, 50]
for i in range(1, len(list1)+1):
    print(list1[len(list1)-i])
print('\n')

# MOST EFFICIENT METHOD
for j in list1[::-1]:
    print(j)


print('\n')
nlist = reversed(list1)
for k in nlist:
    print(k)
print('\n')
