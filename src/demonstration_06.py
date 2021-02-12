"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    tally = 0
    vowels = ["a", "e", "i", "o", "u"]
    
    for data in input_str:
        if data in vowels:
            tally = tally + 1
            
    return tally
            

# UPER - Understand Plan Execute Reflect


print(get_count('shoop'))
print(get_count('saehooiip'))