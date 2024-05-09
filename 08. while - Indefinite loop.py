#while - INDEFINITE LOOP
#PROGRAM 1:
print('program 1: /n')
n=5
while n>0:
    print(n)
    n=n-1
print('Blast off!')

#PROGRAM 2:
print('/n program 2:')
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

#PROGRAM 3:
print('/n program 3:')
print('Using # sign at the start of the sentence wont print the sentence. It will take you back to the loop. If you type done. You exit the loop.')
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')