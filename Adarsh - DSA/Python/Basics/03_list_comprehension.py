# to create a new list from prev list on a condition

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# rather use this using list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x for x in fruits if "a" in x]
print(newlist1)