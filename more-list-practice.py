# Use the following list to complete the following exercises:
us_states = ["Alabama", "Alaska", "Arizona", "Arkansas", 
"California", "Colorado", "Connecticut", "Delaware", 
"Florida", "Georgia", "Hawaii", "Idaho", 
"Illinois", "Indiana", "Iowa", "Kansas", 
"Kentucky", "Louisiana", "Maine", "Maryland", 
"Massachusetts", "Michigan", "Minnesota", "Mississippi", 
"Missouri", "Montana", "Nebraska", "Nevada", 
"New Hampshire", "New Jersey", "New Mexico", "New York", 
"North Carolina", "North Dakota", "Ohio", "Oklahoma", 
"Oregon", "Pennsylvania", "Rhode Island", "South Carolina", 
"South Dakota", "Tennessee", "Texas", "Utah", 
"Vermont", "Virginia", "Washington", "West Virginia", 
"Wisconsin", "Wyoming"]

# 1. Write the code below that verifies the amount (length) of US States!
print(len(us_states))

# 2. create a variable my_state_index and assign the index value of the state you currently reside in
my_state_index = us_states.index("California")

# 3. let's see if you were right.. uncomment below and run. Do you see your state?
print("My state is: " + us_states[my_state_index])

# 4.Using your state index, let's emphasize some importance to it by *upper*casing it.
    # ASSIGN us_state with my_state_index with us_state of my_state_index with the UPPER method
us_states[my_state_index] = us_states[my_state_index].upper()

# PRINT us_state to see if there is a change in your state
print(us_states)

# 5. POOF. You've been promoted to President! Let's add a new state. I like my list to be alphabetical (which it is)
# So let's go ahead and create a state that starts with Z and append it to the end of the list.
us_states.append("Zimbabwe")
print("I appended: " + us_states[50])
print(len(us_states))

# 6. There is no state that begins with B! Lets create one and INSERT it appropriately. (There are 4 A states.)
us_states.insert(4, "Bermuda")
print("I inserted: " + us_states[4])
print(len(us_states))

# 7. Does anyone live in Iowa? Do you know anyone that lives there? Is it even real?! Remove it.. Do it president.
us_states.remove("Iowa")
print(us_states)