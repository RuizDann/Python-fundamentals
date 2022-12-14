# Use the following list to complete the following exercises:

lowercase = ['a', 'b', 'c', 'd', 'e',
             'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

# EASY
# 1. loop through the lowercase and print each element
for letter in lowercase:
    loc = lowercase.index(letter)
    print(f'{loc + 1}: {letter}')

# 2. loop through the lowercase and print the capitalization of each element
for letter in lowercase:
    loc = lowercase.index(letter)
    print(f'{loc + 1}: {letter.upper()}')

# MEDIUM
# 1. create a new variable called uppercase with an empty list
uppercase = []

# 2. loop through the lowercase list
    # 2a. append the capitalization of each element to the uppercase list
for letter in lowercase:
    uppercase.append(letter.upper())
print(uppercase)

# HARD
# A safe password has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.
    # password = "MySuperSafePassword!@34"
    # special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# 1. create the following variables and assign them Booleans as False
    # has_uppercase
    # has_lowercase
    # has_number
    # has_special_char
    
# 2. loop through the string password (same as a list)
    # OR you can create a new list variable of the string password
# using list(string) NOTE: assign it a new variable as such:
    # password_list = list(password) prior to looping.

# 3. For each iteration of the loop, create a if statement
# check to see if it exists in any of the list by using IN
# if it does exist, update the appropriate variable and CONTINUE
# not break.
# NOTE: to see if it has a number, use range from 0 - 10!

# 4. do a final check to see if all of your variables are TRUE
# by using the AND operator for all 4 conditions. (This is done for you, uncomment below)

# final_result = has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True

# NOTE: we can shorthand this by just checking if the variable exists (returns True)
#final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
# this will fail the same if any one of them is False

# If the final_result is true, print "SAFE STRONG PASSWORD"
# else, print "Update password: too weak"
# NOTE: this must be done outside of the loop

password = "MySuperSafePassword!@34"
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

has_uppercase = False
has_lowercase = False
has_number = False
has_special_char = False
final_result = False

if (len(password) >= 4):
    for i in password:
        if i.isupper() == True:
            has_uppercase = True
            
        elif i.islower() == True:
            has_lowercase = True
            
        elif i.isdigit() == True:
            has_number = True
            
        elif i in special_char:
            has_special_char = True
    
if has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True:
    print("Your password is safe!")
else:
    print("Your password is not safe!")

# BONUS: update the password variable to take in an user input!

password = input("Enter a strong password: ")
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

has_uppercase = False
has_lowercase = False
has_number = False
has_special_char = False
final_result = False

if (len(password) >= 4):
    for i in password:
        if i.isupper() == True:
            has_uppercase = True
            
        elif i.islower() == True:
            has_lowercase = True
            
        elif i.isdigit() == True:
            has_number = True
            
        elif i in special_char:
            has_special_char = True
    
if has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True:
    print("SAFE STRONG PASSWORD")
else:
    print("Update password: too weak")

# NIGHTMARE: in the final check, use another if statement to list why it isn't a strong password!

password = input("Enter a strong password: ")
    # MySuperSafePassword!@34
    # MyPasswordHasNoSpecialChar34
    # MyPasswordHasNoNumber!@
    # mypasswordhasnouppercase!@34
    # MYPASSWORDHASNOLOWERCASE!@34
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

has_uppercase = False
has_lowercase = False
has_number = False
has_special_char = False
final_result = False

if (len(password) >= 4):
    for i in password:
        if i.isupper() == True:
            has_uppercase = True
            
        elif i.islower() == True:
            has_lowercase = True
            
        elif i.isdigit() == True:
            has_number = True
            
        elif i in special_char:
            has_special_char = True
    
if has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True:
    print("SAFE STRONG PASSWORD")
else:
    print("Weak Password")
    if has_uppercase == False:
        print("Update password: You need an uppercase letter")
    elif has_lowercase == False:
        print("Update password: You need a lowercase letter")
    elif has_number == False:
        print("Update password: You need a number")
    elif has_special_char == False:
        print("Update password: You need a special character")
