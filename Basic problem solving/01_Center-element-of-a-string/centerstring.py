# Find center element of a string; returm "Cannot find center element of even string" if string length is even number
a ="spiderman"
s = int(len(a))
if(s%2 == 0):
    print("Cannot find center element of even string")
else:
    k = int(s/2 -0.5) # k = 9/2 = 4.5 - 0.5 = 4
    print(a[k])