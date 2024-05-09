#TRY AND EXCEPT CONDITIONAL STATEMENT
while True:
    rawstr = input('Enter a number:')
    try:
        ival = int(rawstr)
    except:
        ival = -1
    if ival>0:                             
        print('Nice work!')
        break
    else:
        print('Please enter a numeric input')
        continue
 