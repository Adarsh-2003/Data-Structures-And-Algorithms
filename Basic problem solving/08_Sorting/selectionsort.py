# s1 : get the first element of the arr and swap it with the min element of the arr
# s2 : lower the size of the an array (exclude 1st element)
# s3 : repeat s1 for the new arr
# s4 : lower the size of the an array (exclude 1st & 2nd element)
# repeat until 2nd last element

arr = [ 89, 23, 56, 78, 36, 35 ]
print(arr)
n = len(arr)

for i in range (n ):
    mini = i
    for j in range (i, n ):
        # getting the minimum element index
        if(arr[j] < arr[mini]):
            mini = j
            
    # swapping the first and the min element
    temp = arr[i]
    arr[i] = arr[mini]
    arr[mini] = temp
    
print(arr)
    
# try to add i+1 in the inner j loop
# increases efficiency as comparing the first element with itself is unncessary and absurd