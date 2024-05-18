numbers = [12, 75, 150, 180, 145, 525, 50]
list1 = list()

for num in numbers:
    if 150 < num <= 500:
        continue
    elif num > 500:
        break
    if num % 5 == 0:
        list1.append(num)

print(list1)
