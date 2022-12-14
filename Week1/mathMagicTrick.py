# We will replicate a number magic trick with Python! Below is the magic trick that we will convert! Below that is the python instructions, you will need to complete.

# Step 1: Pick a number from 1 - 9
# Step 2: Multiple by 2
# Step 3: Add 10 to the total
# Step 4: Divide by 2
# Step 5: Subtract by the original number
# Final Number: 5

# assign a variable "step_1" to a number of your choice between 1 - 9
# assign a variable "step_2" to the product of step_1 and the number 2
# assign a variable "step_3" to the sum of step_2 and the number 10
# assign a variable "step_4" to the quotient of step_3 and the number 2
# assign a variable "step_5" to the difference between step_4 and step_1
# print step_5 and you should see 5!

# Easy Solution:
import random

randNum = random.randint(1, 9)
newNum = randNum * 2
newNum += 10
newNum /= 2
newNum = newNum - randNum

print(f'Final number: {int(newNum)}\n')

# BONUS 1: can you convert step_1 to prompt a user's input?
    # HINT: you need to cast step_1 to a int because user input is a type string.
    # (**** Make it 2 variables 1 for input, 1 for the steps ****)

userInput = ['', '']

userInput[0] = int(input('Enter a number between 1 and 9:\t'))

userInput[1] = userInput[0] * 2
userInput[1] += 10
userInput[1] /= 2
userInput[1] = userInput[1] - userInput[0]

print(f'Final number: {int(userInput[1])}\n')

# BONUS 2: can you use a single variable?

userNum = [0, 0]

while True:
    userNum[0] = int(input("Enter a number between 1 and 9:\t"))
    
    if 1 <= userNum[0] <= 9:
        break
    else:
        print("Input must be an integer between 1 and 9.")

userNum[1] = userNum[0] * 2
userNum[1] += 10
userNum[1] /= 2
userNum[1] = userNum[1] - userNum[0]

print(f'Final number: {int(userNum[1])}\n')