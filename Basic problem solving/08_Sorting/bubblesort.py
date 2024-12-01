# get the arr
# 2 loops 1st for iterating the main array
#              2nd for iterating inside the array for compare and swap optn
# decrease the size of the selected array from the end

arr = [20, 40, 10, 9, 30]
size = len(arr)
for i in range(size):
    swapped = False
    for j in range(0, size - i - 1):
        if (arr[j] > arr[j+1]):
            arr[j], arr[j+1] = arr[j+1] , arr[j]
            swapped = True
    if not swapped:
        break
print(arr)