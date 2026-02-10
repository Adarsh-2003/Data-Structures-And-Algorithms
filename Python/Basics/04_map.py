# the map function similar to map func in js

# use to convert string numbers in a list to int number in list
# eg :- ['1', '2', '3'] -> [1,2,3]

lst = ['1', '2', '3']
lst = list(map(int, lst))
print(lst)   # [1, 2, 3]

# it is neccessary to wrap using list() function 
# s = ['1', '2', '3', '4']
# res = map(int, s)
# print(res)  #// <map object at 0x0000015AAFE65C60>

# user defined function on map function
a = [1, 2, 3, 4]
def double(val):
  return val*2

res = list(map(double, a))
print(res) # [2, 4, 6, 8]

# int to str of a list
nums = [1,2,3]
result = map(str, nums)
print(list(result))
