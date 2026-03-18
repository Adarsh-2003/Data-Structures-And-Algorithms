# Task 4: The "Age Validator" (Raising Exceptions)
# Write a program that asks for a user's age.

# The Goal: Use a try block to check if the age is between 0 and 120. If the age is negative or over 120, use the raise keyword to trigger a ValueError with a custom message like "That's not a human age!"

# Requirement: Catch that specific error in an except block and display your custom message.

try :
    inp = int(input("Enter your age "))

    def age_check(inp):
        if not 0 <= inp <= 120:
            raise ValueError("That's not a human age")
        
    age_check(inp)

except ValueError as e:
    print(e)