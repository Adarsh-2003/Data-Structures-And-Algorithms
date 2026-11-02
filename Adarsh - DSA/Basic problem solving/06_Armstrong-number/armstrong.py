# 153 is a armstrong number
# (1 x 1 x 1) + (5 x 5 x 5) + (3 x 3 x 3) = 153

summ = 0

while(num > 0):
  digit = num % 10 # get the last digit
  summ += pow(digit, 3) # cube it
  num = num // 10 # reduce the number i.e cut off the last digit

print(summ)


# own solution (prereq map function in random things)
# converts a number to a string list -> to num list -> to ease the access of checking armstrong number,
num = 407
lst = list(str(num))
lst1 = list(map(int, lst))
sum = 0
for i in range(len(lst1)):
  sum += pow(lst1[i],3)

print(sum)