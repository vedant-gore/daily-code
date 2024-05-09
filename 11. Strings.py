#STRINGS
print('Program 1:')
fruit='banana'
letter=fruit[1]
print('letter')

print('Program 2:')
x=3
w=fruit[x-1]
print(w)

print('Program 3:')
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index, letter)
    index=index+1

print('Program 4:')
for letter in fruit:
    print(letter)

print('Program  5:')
word='banana'
count=0
for letter in word:
    if letter == 'a':
        count=count+1

print(count)

print('Program 6: SLICING')
s='monty python'
print(s[0:4])
print(s[6:7])
print(s[:2])
print(s[8:])
print(s[:])

print('Program 7:')
a='Hello'
b=a+'there'
print(b)
c=a+' '+'there'
print(c)

print('Program 8:')
fruit2='banana'
'n' in fruit2
'm' in fruit2
'nan' in fruit2
if 'a' in fruit2:
    print('fount it')
    
print('Program 9:')
greet='Hello Bob'
zap=greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

print('Program 10:')
fruit='banana'
posn=fruit.find('na')
print(posn)
aa=fruit.find('z')
print(aa)

print('Program 11:')
greet='Hello Bob'
nstr=greet.replace('Bob','Jane')
print(nstr)

print('Program 12:')
data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos=data.find('@')
print(atpos)
sppos=data.find(' ',atpos)
print(sppos)
host=data[atpos+1:sppos]
print(host)
