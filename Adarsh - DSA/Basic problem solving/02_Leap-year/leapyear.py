def is_leap(year):
    leap = False
    if (year %400==0):
        leap = True
    elif(year %4==0 and year %100!=0): # including 100 will sort years which are centuric
        leap = True
    return leap

year = int(input())
print(is_leap(year))

'''
A year is leap year if its divisble by 4 with an exception for century years
Exception : For century year to be a leap yearit must be divisible by 400
eg. 2024 is a leap year ( divisible by 4)
eg. 1900 is NOT a leap  year even though it is divisible by 4 coz it falls under 
    the century exception
eg. 2000 is a leap year ( divisible by 400 by exception)
'''