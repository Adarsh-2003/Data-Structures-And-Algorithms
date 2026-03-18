# Task 1: The "Safe" Indexer
# Create a list of five colors. Write a program that asks the user for an integer and prints the color at that index.

# The Goal: Use a try-except block to catch IndexError (if the number is too high) and ValueError (if they type "blue" instead of "3").

# Bonus: Use a finally block to say "Thanks for playing!" regardless of the outcome

list1 = ['red', 'black', 'yellow', 'orange', 'pink']

try :
    inp = int(input("Enter a number "))
except IndexError:
    print("Number too high")
except ValueError:
    print("Invalid input")
else:
    print(list1[inp])
finally:
    print("Thanks for playing!")