'''
Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
Do not convert the integer into a string.
'''

def palin(num):
    reversed_num = 0
    origional_num = num
    num = abs(num)
    while num != 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num //= 10
    return origional_num == reversed_num

num = 121
print(palin(num))
num = -121
print(palin(num))
