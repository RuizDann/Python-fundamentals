# 1. 
    # a. run the following function and examine the behavior of the function return

def print_greeting():
    greetings = "hello"
    print(greetings)

# run it here!
print_greeting()
    # b. Convert this implicit return function to an explicit return function!
def print_greeting2():
    greetings = "salutations"
    return greetings
    
    # c. Run the newly printed code! (Examine NOTHING is printed to the terminal!)

# run it here!
print_greeting2()
    # d. Create a variable my_greeting and store the return value of return_greeting then print the variable!
myGreeting = print_greeting2()

print(myGreeting)