def squares(x):
    return x * x

list1 = [1,2,3,4]
newl = []
for num in list1:
    newl.append(squares(num))
    
print(newl)