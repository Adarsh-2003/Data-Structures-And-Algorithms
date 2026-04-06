list1 = [1,2,3,4]
list2 = list1
list1[0] = 10

print(list1)  # Output: [10, 2, 3, 4]
print(list2)  # Output: [10, 2, 3, 4]

# list2 is a reference to list1, so changes to list1 affect list2

# if we use .copy() method then the changes will not be reflected in list2

list1 = [1,2,3,4]
list2 = list1.copy()
list1[0] = 10

print(list1)  # Output: [10, 2, 3, 4]
print(list2)  # Output: [1, 2, 3, 4]

# .copy() method on nested list
list1 = [1,2,3,[11,22]]
list2 = list1.copy()
list1[3][0] = 10

print(list1)  # Output: [10, 2, 3, 4]
print(list2)  # Output: [1, 2, 3, 4]