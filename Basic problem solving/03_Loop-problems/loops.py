# Problem 1
# After flipping a coin 10 times you've got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
counter =0
for res in result:
    if res == "heads":
        counter +=1
print(f"heads occured {counter} times")

# Problem 2
# Print square of all numbers between 1 to 10 except even numbers
for i in range(10):
    if i%2 != 0:
        print(i*i)

# Problem 3
# Track your expense and show the relative month
expense_list = [2340, 2500, 2100, 3100, 2980]
user = int(input('Enter the expense '))
found = False
for expense in expense_list:
    if user == expense:
        found = True
        print(f"Expense in the {expense_list.index(expense) + 1} month ")
        break
if not found:
    print('Expense not found ')

# Problem 4
# Lets say you are running a 5 km race. Write a program that,
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
        

for i in range(5):
    user = input('Are you tired ? ')
    if user == 'yes':
        print('You didnt complete the race')
        break
    elif user == 'no':
        pass
    else:
        print('What do you mean ?')
        break
    
    if i==4:
        print('Congratulations you won ')