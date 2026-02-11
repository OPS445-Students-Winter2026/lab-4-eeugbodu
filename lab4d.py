#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    
    return(s[:5])

def last_seven(s):

    return(s[-7:])



def middle_number(num):
    if isinstance(num, float):
        str_num = f"{num:.2f}"
    else:
        str_num = str(num)
    numLen = len(str_num)
    mid = numLen // 2

    if numLen % 2 == 0:
        return(str_num[mid-1  : mid+1])
    
    else:
        return(str_num[mid])

def first_three_last_three(s1, s2):
    return(s1[:3] + s2[-3:])


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))