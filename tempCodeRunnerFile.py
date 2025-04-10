list1 = [1,2,3,4]
list2 = list1.copy()
list1[0] = 10

print(list1)  # Output: [10, 2, 3, 4]
print(list2)  # Output: [10, 2, 3, 4]