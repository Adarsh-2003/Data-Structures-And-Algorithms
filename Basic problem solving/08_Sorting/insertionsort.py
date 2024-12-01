# insertion sort

arry = [1,5,34,2,4,11]
n = len(arry)

for i in range(1,n):
  key = arry[i] # storing the 2nd elmt in key
  j=i-1 # j as helper
  while(j>=0 and key < arry[j]): # weird af condition
    arry[j+1]=arry[j] # assigning 2nd elm as 1st elem 
    # i.e 5 = 1
    j-=1 # weird minus in j
  arry[j+1]=key # regaining the value from key jesus
print(arry)