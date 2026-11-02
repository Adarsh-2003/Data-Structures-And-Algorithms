def fact(x):
    if (x==0):
        return 1
    return x * fact(x-1)
res = fact(5)
print(res)

# a function which calls itself

# 5 * fact(5-1)
 