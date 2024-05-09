#LISTS 
print('Program 1: List examples')
print([1,24,76])
print(['red', 24, 98.6, [5,6]])
print([])

print('Program 2:')
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])

print('Program 3: Changing elements of lists')
fruit = 'Banana'
x = fruit.lower()
print(x)
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

print('Program 4: Length of lists')
print('The length of list friends is:',len(friends))  # len() functtion will give me the number of elements in the list as they are numbered exactly like strings. But in strings, each character has an index number
print('Program 5: Using range function')
print(range(4))
friends2 = ['Joseph', 'Glenn', 'Sally']
print('The length of list friends2 is:', len(friends2))
print('The range of length of list friends2 is:', range(len(friends2)))

print('Program 5: Using for loop for lists')
for friend in friends:
    print('HNY:', friend)
    
count = 0
for i in range(len(friends)):
    friend = friends[i]
    count = count+1
    print(count, 'HNY:', friend)
    
print('Program 6: Building list from scratch')
# create empty list
# add elements using append()
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

print('Program 7: FINDING ELEMENTS in list')
some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)

print('Program 8: Sorting elements in lists')
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)

print('Program 9:BUILT-IN functions')
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total+value
    count = count+1
    
avg = total/count
print('Avg: ', avg)

numlist = list()
while True:
    inp2 = input('Enter a number: ')
    if inp2 == 'done':
        break
    value = float(inp2)
    numlist.append(value)

avg2 = sum(numlist)/len(numlist)
print('avg:', avg2)

print('Program 10: SPLITTING Lists and strings')
abc = 'with three words'
stuff2 = abc.split()
print(stuff2)

line = 'a lot       of spaces'
etc = line.split()
print(etc)

line2 = ('first;second;third')
thing = line2.split()
print(thing)
print(len(thing))
thing = line2.split(';')
print(thing)
print(len(thing))

fhand = open('mbox-short.txt')
for line3 in fhand:
    line3 = line3.rstrip()
    if not line3.startswith('From '):
        continue
    day = line3.split()
    print(day[2])
    
print('Program 11: DOUBLE SPLIT PATTERN')
line4 = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words3 = line4.split()
email = words3[1]
pieces = email.split('@')
print(pieces)
print(pieces[1])