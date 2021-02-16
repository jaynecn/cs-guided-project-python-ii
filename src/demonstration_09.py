"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
def get_middle(input_str):
    # need variable to add to 
    result = ""
    
    # get data on the length of the string
    length = len(input_str)
    
    # if the string length is an odd number:
    if length % 2 != 0:
        # return string character with index:
        # divide by two and then round the number down to the nearest integer 
        return input_str[len(input_str)//2]

    # if the string is length is an even number
    else:
        # return the two middle string characters with index:
        # divide by two and then round the number down to the nearest integer 
        result = result + input_str[len(input_str)//2 - 1] + input_str[len(input_str)//2]

        return result
    
print(get_middle("testing"))
print(get_middle("test"))
print(get_middle("middle"))
print(get_middle("A"))


