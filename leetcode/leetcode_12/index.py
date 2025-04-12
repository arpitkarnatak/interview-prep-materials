import sys
sys.stdin = open('./leetcode_12/input.txt', 'r')
sys.stdout = open('./leetcode_12/output.txt', 'w')

'''
Integer to Roman:
https://leetcode.com/problems/integer-to-roman/
'''


symbols = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}


def stringBuilder(stringSoFar, numberLeft):
    if numberLeft == 0:
        return stringSoFar
    for symbol in list(symbols.keys())[::-1]:
        if symbol <= numberLeft:
            return stringBuilder(stringSoFar + symbols[symbol], numberLeft - symbol)
    return 0

def integerToRoman(nums):
    return stringBuilder("", nums)

num = int(input())
print(integerToRoman(num))
