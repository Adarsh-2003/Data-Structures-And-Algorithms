# standard way of printing count of digits of a number
num = 1234
count = 0
while num > 0:
    num //= 10
    count+=1

print(count)

# another way of printing count of digits of a number
num = 23445
print(len(str(num)))

# Time complexity of both the above methods is O(log n).
# bcoz of repetitive division //