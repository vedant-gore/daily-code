x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
y = (1, 9, 2)
print(y)
print(max(y))

print('\n PROGRAM 1: TUPLES AND ASSIGNMENT')
(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)

print('\n PROGRAM 2: TUPLES AND DICTIONARIES')
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)
tups = d.items()
print(tups)

print('\n PROGRAM 3: TUPLES ARE COMPARABLE')
print((0, 1, 2) < (5, 1, 2))
print(('Jones', 'Sally') < ('Jones', 'Sam'))

print('\n PROGRAM 4: SORTING LISTS OF TUPLES')
d = {'a': 10, 'b': 1, 'c': 22}
d.items()
sorted(d.items())

'\n'
print('\n SORTING BY KEYS:')
d = {'a': 10, 'b': 1, 'c': 22}
t = sorted(d.items())
print(t)
for k, v in sorted(d.items()):
    print(k, v)

print('\n SORTING BY VALUES:')
c = {'a': 10, 'b': 1, 'c': 22}
temp = list()
for k, v in c.items():
    temp.append((v, k))
print(temp)
temp = sorted(temp, reverse=True)
print(temp)

print('\n\n PROGRAM 4: FINAL PROGRAM')
fhand = open('mbox.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

lst1 = list()
for key, val in counts.items():
    newtup = (val, key)
    lst1.append(newtup)

lst1 = sorted(lst1, reverse=True)

for val, key in lst1[:10]:
    print(key, val)

print('\n EVEN SHORTER VERSION!!!')
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v, k) for k, v in c.items()]))