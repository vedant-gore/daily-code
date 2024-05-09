#for - DEFINITE LOOP
#PROGRAM 1:
print('Program 1:')
for i in [5,4,3,2,1]:
    print(i)
print('Blast off!')
 
print('Program 2:')
friends = ['Vedant','Shreya','Didi']
for friend in friends:
    print('Welcome!', friend)

print('Program 3: Finding the largest value')
largest_so_far = -1
nums = [9,41,12,3,74,15]
for num in nums:
    if largest_so_far < num:
        largest_so_far = num
    print(largest_so_far, num)
print('After', largest_so_far)

print('Program 4: Counting')
count = 0
nums = [9,41,12,3,74,15]
for num in nums:
    count = count+1
    print(count, num)
print('Counting:', count)

print('Program 5: Addition')
sum = 0
nums = [9,41,12,3,74,15]
for num in nums:
    sum = sum+num
    print(sum, num)
print('Addition:',sum)

print('Program 6: Average')
count = 0
sum = 0 
print('Before:', count, sum)
nums = [9,41,12,3,74,15]
for num in nums:
    count = count+1
    sum=sum+num
    print(count,sum)
print('Average is:', float(sum/count))

print('Program 6: Filtering')
nums = [9,41,12,3,74,15]
for num in nums:
    if num>20:
        print('large',num)
 
print('Program 7: Search using boolean variable:')
nums=[9,41,12,3,74,15,3,12,13,31,3,3,]
count2=0
for num in nums:
    found=False
    if num==3:
        count2=count2+1
        found=True
    print(found,num)
print('found 3:',count2)

print('Finding smallest:')
smallest = None
nums = [9,41,12,3,74,15]
for num in nums:
    if smallest is None:
        smallest=num
    elif smallest>num:
        smallest=num
    print(smallest, num)
print('After', smallest)