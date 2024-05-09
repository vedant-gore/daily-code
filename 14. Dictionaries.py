purse = dict()
purse['money'] = 12
purse['candy'] = 3
print(purse)
purse['candy'] = purse['candy'] + 2
print(purse)

j = {'chuck': 1, 'fred': 42, 'jan': 100 }
print(j)
o = {}
print(o)

print('\n PROGRAM 1: COUNTING ELEMENTS IN A DICTIONARY')
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name]+1
print(counts)

print('\n THE get() METHOD')
if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get(name, 0)

print('\n ACTUAL get() METHOD PROGRAM')
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for n in names:
    counts[n] = counts.get(n, 0)+1

print(counts)

print('\n PROGRAM 2: COUNTING PATTERN')
counts = dict()
print('Enter a line of text: ')
line = input()

words = line.split()
print('words:', words)

print('Counting...')
for words in words:
    counts[words] = counts.get(words, 0)+1
print('counts:', counts)

print('\n\n PROGRAM 3: DEFINITE LOOPS AND DICTIONARIES')
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key], end=' ')

print('\n\n PROGRAM 4: RETRIEVING LISTS OF KEYS AND VALUES')
j = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(j))      # creates a list of keys
print(j.keys())     # creates a list of keys
print(j.values())   # creates a list of values of keys
print(j.items())    # creates a list of tuples with keys and values'
for a, b in j.items():
    print(a, b)

print('\n PROGRAM 5: FINAL PROGRAM')
name4 = input('Enter file name: ')
handle = open(name4)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)



