# Dictionary
# create a new dictionary named my_person with one key value pair of name : [YOUR_NAME]
my_person = {
    "Name": "Daniel Ruiz"
}

# verify the type of my_person to be a dictionary by using type
print(type(my_person))
# Next we will use a pre-made dictionary:

person_1 = {
    "first_name": "Scooby",
    "favorite_snack": "Rare Candy",
    "wears_glasses": True
    }

print(person_1.keys())
print(person_1.values())

# add a key value pair to person_1 with the last_name of Doo
person_1["last_name"] = "Doo"
# update person_1 favorite_snack to "Scooby Snacks"
person_1.update({"favorite_snack": "Scooby Snacks"})
# Remove the "wears_glasses" key:value from person_1
del person_1["wears_glasses"]

print(person_1.keys())
print(person_1.values())