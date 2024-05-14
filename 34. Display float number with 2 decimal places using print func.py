def mytrunc(numb, decp):
    pos1 = numb.find('.')
    str1 = numb[:pos1+decp+1]
    return str1


inp1 = input('Enter your decimal number: ')
inp2 = input('Enter how much decimal places you want: ')
inp2 = int(inp2)
print(mytrunc(inp1, inp2))

#OR
# print('%.2f'%num)
