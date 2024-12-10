# 0,1,1,2,3,5,8,13

n = 7
num1 = 0
num2 = 1
print(num1)
print(num2)

for i in range(n):
    num3 = num1 + num2
    num1, num2 = num2, num3 # tuple unpacking
    print(num3)


# sensible if user needs only top 7 fibo 
# n = 7
# num1 = 0
# num2 = 1
# print(num1)
# print(num2)

# for i in range(n-2):
#     num3 = num1 + num2
#     num1, num2 = num2, num3 # tuple unpacking
#     print(num3)
