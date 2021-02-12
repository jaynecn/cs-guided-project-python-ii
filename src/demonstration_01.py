"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""


def last(a, n):
    emptyList = []
    if n == 0:
        return emptyList
    elif n > len(a):
        return "invalid"
    else:
        return a[-n:]
    
print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7))
print(last([1, 2, 3, 4, 5], 0))

my_list = [4, 3, 9, 9, 7, 6, 12]
               
# accessing one individual element
print(my_list[4])

# access the last element in the list
print(my_list[-1])

# Getting subarrays

# get the first 3 elements
print(my_list[0:3])
    


