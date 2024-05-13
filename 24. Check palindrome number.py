def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        remainder = number % 10
        reverse_num = (reverse_num * 10) + remainder
        number = number // 10   #FLOOR DIVISION. TRUNCATES DECIMAL PART AND RETURNS INTEGER

    # check numbers
    if original_num == reverse_num:
        print("Given number is palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)