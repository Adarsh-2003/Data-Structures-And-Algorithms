# 5! = 5 x 4 x 3 x 2 x 1 x 0

x = int(input("number : "))
def factorial(x):
    if x == 0:
        print(1)
    else:
        fact = 1
        for i in range(1,x+1):
            fact = fact * i
        print(fact)

factorial(x)