# Functions Parameters and Arguments
# Lets take those functions we built in practice_2 and make them more dynamic:
# Rewrite the functions from practice_2 using parameters:
def add_num(x, y):
    plus = x + y
    print(f'{x} plus {y} equals: {plus}')


def subtract_num(x, y):
    sub = x - y
    print(f'{x} minus {y} equals: {sub}')


def multiply_num(x, y):
    mult = x * y
    print(f'{x} times {y} equals: {mult}')


def divide_num(x, y):
    div = round(x / y, 2)
    print(f'{x} divided by {y} equals: {div}')

# Don't forget to call your functions to make sure they work

#Uncomment to call your functions:
# print("I should see the number 7 below from add_num: ")
# add_num(3, 4)

# print("I should see the number -2 below from subtract_num: ")
# subtract_num(6, 8)

# print("I should see the number 18 below from multiply_num: ")
# multiply_num(2, 9)

# print("I should see the number 2.0 below from divide_num: ")
# divide_num(10, 5)

# Extra Time?

# Now take in 2 users inputs and pass them 
# in as arguments when calling the functions
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

add_num(x, y)
subtract_num(x, y)
multiply_num(x, y)
divide_num(x, y)