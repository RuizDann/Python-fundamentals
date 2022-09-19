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

# print the LENgth of us_states
print(len(us_states)) #50
# print the comparison boolean of the LENgth of us_states to 50
if len(us_states) == 50:
    print(True)
else:
    print(False)
# prints True

# create a variable my_state_index and assign the index value of the state you currently reside in
# print us_state with my_state_index to ACCESS your state!

userState = input("Enter your state: ")
userState = userState.title()

for i, state in enumerate(us_states):
    if state == userState:
        my_state_index = i
        print(my_state_index)

# another way to do it
for state in us_states:
  if state == userState:
    print("found it at index: ", us_states.index(state))
    break
  else:
    continue