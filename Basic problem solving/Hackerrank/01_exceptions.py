items = int(input())
for i in range(items):
    try:
        a,b = input().split()
        res = int(int(a) // int(b))
        print(res)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as v:
        print("Error Code:", v)
        
# Input
# 3
# 1 0
# 2 $
# 3 1

# Expected Output
# Error Code: integer division or modulo by zero
# Error Code: invalid literal for int() with base 10: '$'
# 3

# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true