# Write a Python function that takes a list of numbers as input and returns a new list containing only the even numbers.
# For example, if the input is [1, 2, 3, 4, 5, 6], the output should be [2, 4, 6].
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
