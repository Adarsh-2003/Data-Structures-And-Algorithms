# to create a new list from prev list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# rather us this using list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x for x in fruits if "a" in x]
print(newlist1)