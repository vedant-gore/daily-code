mstr = input('Enter your string: ')
sstr = input('Enter the substring: ')
count = mstr.count(sstr)
print(sstr, 'appeared', count, 'times')


def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count


count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")
