def remove_char(string, num_char):
    string = string[num_char:]
    return string


y = input('Number of characters to be removed: ')
Y = int(y)
X = input('Enter the statement: ')
a = remove_char(X, Y)
print('Output is: ', a)
