# declare a VARIABLE named my_favorite_band and ASSIGN it a STRING value of your choice.

myFavBand = "Blink182"

# PRINT a CONCATENATION of the variable and a string literal: " is my favorite band!"

print(myFavBand + " is my favorite band!")

# prompt an user INPUT to ask "What is your favorite color?" and assign it to a variable called "user_favorite_color"

userFavColor = input("What is your favorite color?")

# PRINT a string concatenation with user_favorite_color and "is a nice color!"

print(userFavColor + " is a nice color!")

# Ask user for first and last name and print it out
fName = input("What is you first name?")
lName = input("What is your last name?")

print(fName + " " + lName) # one way of concatenation
print(f'{fName} {lName}') # f string concatenation
print(f'{fName} {lName}'.title()) # makes the first letter in variable capitalized
print(f'{fName} {lName}'.upper()) # capitalizes every letter
