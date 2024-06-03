def has_unique_chars(input_string):
    # Loop through each character in the string
    for i in range(len(input_string)):
        # Check if the character appears again in the rest of the string
        if input_string[i] in input_string[i+1:]:
            return False  # If it does, return False
    return True  # If no duplicates are found, return True

# Test cases
print(has_unique_chars("abcde"))  # Should return True
print(has_unique_chars("hello"))  # Should return False
print(has_unique_chars(""))       # Should return True
