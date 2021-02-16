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
    result = ""
    resultList = []
    test = []
    length = len(input_str)
    print(length)
    if length % 2 != 0:
        for data in input_str:
            resultList.append(data)
            print(resultList)
            maths = 7 // 2
            print(maths)
            print(resultList[maths])
        # return thisResult
    else:
        for data in input_str:
            resultList.append(data)
            # print(resultList)
        
        # had the stuff below here set at the wrong indentation, oops
        test.append(resultList[1])
        test.append(resultList[2])
             
    return test
    
print(get_middle("testing"))
print(get_middle("test"))
# print(get_middle("middle"))


