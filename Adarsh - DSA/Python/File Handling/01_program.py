# This program is about reading a file and counting the maximum occurence of any word and printing the same

# opens the file
f = open("File Handling\\poem.txt", "r")

# created an empty dictionary to hold count and count value 
stats = {}

# iterating through lines
for line in f:
    # splits the line by " " and stores them in an array
    words =  line.split(" ")
    # iterating into the array
    for element in words:
        # iterating into stats dictionary and updating the value of words that is to be stored in the stats dictionary
        if element in stats:
            stats[element] += 1
        else:
            stats[element] = 1

#converting the values of stats dictionary into a list and using max function to calculate max value
max_value = max(list(stats.values()))

# special type of for loop to iterate through key value pairs in the dictionary
for key, value in stats.items():
    if value == max_value:
        print("Max value key is : ", key)

# can also be solved by list comprehension
