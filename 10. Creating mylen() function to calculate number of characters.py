#creating a function to calculate length of the string
def mylen(string):
    count=0
    for x in string:
        count=count+1
        if x== ' ':         #REDUCTION OF WHITE SPACE
            count=count-1
    return count
    
y = mylen(input('Enter the sentence of which you want to calculate the number of characters:'))
print(y)
print(type(y))