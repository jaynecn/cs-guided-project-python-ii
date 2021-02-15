"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"
"""
def repeat_it(input_str):
    result =""
    for data in input_str:
        multipleNumber = input_str.index(data)
        # print(multipleNumber)
        result = result + data.upper() + (data.lower() * multipleNumber) + "-"
        newResult = result[:-1]
        # print(newResult)
    # seperate by the dash
    
    return newResult
    # get the index number of the item
    
    
    # repeat it by the number it is in the index plus "-"
    # Your code here


print(repeat_it("abcd"))
print(repeat_it("RqaEzty"))
print(repeat_it("cwAt"))