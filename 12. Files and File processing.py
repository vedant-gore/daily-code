#FILES AND PROCESSING FILES
print('Program 1:') 
fhand = open('mbox.txt')
print(fhand)

print('Program 2:')
xfile = open('mbox-short.txt')
for cheese in xfile:
    print(cheese)

print('Program 3:')
fhand = open('mbox-short.txt')
count = 0
for x in fhand:
    count = count+1
print('Line count:', count)

print('Program 4:')
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

print('Program 5:')
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)

print('Program 6:')
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

print('Program 7:')
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

print('Program 8:')
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
    
print('Program 8:')
fname = input('Enter the file name: ')
fhand = open(fname)
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count = count+1
print('There were', count, 'subject lines in', fname)

print('Program 9:')
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File name cannot be found: ', fname)
    quit()
    
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count = count+1
print('There were', count, 'subject lines in', fname)