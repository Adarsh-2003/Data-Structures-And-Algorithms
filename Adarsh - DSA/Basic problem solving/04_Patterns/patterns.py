for i in range(4):
    for j in range(4):
        print("* ", end="")
    print()

"""

* * * * 
* * * * 
* * * * 
* * * * 

"""
# ----------------------------------------------------------------

for i in range (1,5):
    for j in range (i):
        print("* ", end="")
    print()

"""

# as i is initializing from 1 to 5 so we direct j as i which implies start printing times
like for the 1st row 1 number of times the start prints

* 
* * 
* * * 
* * * * 

"""
# ----------------------------------------------------------------

for i in range(1,5):
    for j in range(i):
        print(j+1,end="")
    print()


"""

the number in each row is nothing but the number of row

1
22
333
4444

"""

# ----------------------------------------------------------------

for i in range(4):
    for j in range(4-i):
        print("* ", end="")
    print()

"""

to print stars upside down start the inner row iteration from n => row count (provide in qs) and reduce by i (as i keeps reducing as we decend by row)

* * * * 
* * * 
* * 
* 

"""

# ----------------------------------------------------------------

for i in range(5):
    for j in range(5-i):
        print(j+1, end="")
    print()

"""

as we need increasing number in each row we will use j (iteration in the inner loop ) and reduce by i as we need to decrease number count of each element
in the row as we decend

12345
1234
123
12
1

"""

# ----------------------------------------------------------------


n = 5
for i in range(1, n + 1):
  for j in range(i):  # Iterate from 0 to i-1 (inclusive)
    print(i, end="")
  print()


"""

just printing i as it denotes row count

11111
2222
333
44
5

"""
n=5
for i in range(0,n):
    #space
    for k in range(n-i-1):
        print(" ",end='')

    #star
    for j in range(2*i+1):
        print("*",end="")

    #space
    for k in range(n-i-1):
        print(" ",end='')
    print()

"""

    *    
   ***   
  *****  
 ******* 
*********

[space star space]

[4, 1, 4]
[3, 3, 3]
[2, 5, 2]
[1, 7, 1]
[0, 9, 0]

"""