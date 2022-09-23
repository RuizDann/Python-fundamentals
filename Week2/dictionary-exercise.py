# 1. Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 0
}

# SCENARIO: A person came in and bought one of everything!

for key, value in inventory.items():
    # decrement item by using an assignment operator
    # NOTE: recall that item represents the key of the key:value pair
    if value == 0:
        print(f'Sorry {key} is currently out of stock.')
    else:
        value -= 1
    print(f'{key}: {value}')
        


# 2. Implicit Functions 
# (When we work with global variables/objects and don't return anything, 
# these functions are implicit return functions!)

user_1 = {
    "firstName": "Stephanie",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "95485"
}

user_2 = {
    "firstName": "Brion",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "67344"
}

user_3 = {
    "firstName": "Daniel",
    "lastName": "Kim",
    "role": "Instructor",
    "id": "74324"
}
    # a. Dictionaries - create a function that takes in a dictionary which updates the "role" key value pair and makes it uppercase
def role_to_upper(user):
    for key, value in user.items():
        if key == "role":
            user.update({key: value.upper()})
        else:
            continue
    print(user.items())
    

    # b. Dictionaries - Run the functions (3 times, 1 for each user!)
role_to_upper(user_1)
role_to_upper(user_2)
role_to_upper(user_3)

instructor_list = [user_1, user_2, user_3]
# print(instructor_list)

    # c. List - create a function that takes in the list and 
    # checks if the each user's role is equal to "INSTRUCTOR". 
# if it is the same, print VALID else print INVALID (try to use a loop here!)
def role_upper_checker(list):
    for user in list:
        for key, value in user.items():
            if key == "role":
                if value == value.upper():
                    print("VALID")
                else:
                    print("INVALID")
            else:
                continue

role_upper_checker(instructor_list)
    
    # d. import the random module and update the function to re-assign the id of each user
        # user["id"] = random.randomint(1000, 9999)
    # e. don't forget to run it!
import random    

def id_to_random(list):
    for user in list:
        for key in user.keys():
            if key == "id":
                user.update({key: random.randint(1000, 9999)})
            else:
                continue
    print(list)
id_to_random(instructor_list)

# 3. Explicit Functions
user_info = [46453, "Devin", "Smith"]
    # Each element by index of user_info follows the format of: id, first_name, last_name
    # Create a function with a parameter user_list
    #   - return a dictionary with the follow key value pairs:
    #   - id: user_list[0]
    #   - first_name: user_list[1]
    #   - last_name: user_list[2]

user_dict = {}
# check if dictionary is empty
print(user_dict.items())

def list_to_dict(user_list):
    key_list = ["id", "first_name", "last_name"]
    for index in range(0, len(user_list)):
        user_dict.update({key_list[index]: user_list[index]})

# runs the function
list_to_dict(user_info)

# check to see if dictionary is now filled
print(user_dict.items())