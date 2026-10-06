imran = {
  "name": "Imran",
  "age": 22,
  "preferred_operating_system": "Ubuntu",
}

eliza = {
  "name": "Eliza",
  "age": 34,
  "preferred_operating_system": "Arch Linux",
}


print(imran["name"])
print(imran["address"]) 
# They don't need to suggest a fix
# # But they could comment out this line,
# # add an address value to the object
# # or convert it into a class

# TASK 5:
# This code contains some untyped objects.
# Try checking it with mypy before running the code and predict what you think will happen when you run the code.
#
# Prediction:
#
# Can you explain what actualy happens?
#
# There is no visible error from mypy.
# Running the code gives us a KeyError.
# Something like:
# mypy / typing checks types only, not the type of values within other objects or classes, unless they are explicitly specified and checked.
