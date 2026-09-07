person1 = Child("Elizaveta", "Alekseeva")
# Prediction: Creates instance of Child class with first name "Elizaveta" and last name "Alekseeva".
print(person1)
print(person1.first_name)
print(person1.last_name)
# Outcome: As expected.


print(person1.get_name())
# Prediction: Child inherits Parent methods, therefore calls get_name method: "Elizaveta Alekseeva"
# Outcome: As expected.

print(person1.get_full_name())
# Prediction: Calls get_full_name on child, no previous names: "Elizaveta Alekseeva"
# Outcome: As expected.

person1.change_last_name("Tyurina")
# Prediction: Changes last_name to "Tyurina", and previous_last_names to ["Alekseeva"], returns nothing
print(person1.last_name)
print(person1.previous_last_names)
# Outcome: As expected.

print(person1.get_name())
# Prediction: Child inherits Parent methods, therefore calls get_name method: "Elizaveta Alekseeva"
# Outcome: As expected.

print(person1.get_full_name())
# Prediction: Returns first_name last_name (née previous_last_names[0]) (original last name) 
# ""Elizaveta Tyurina (née Alekseeva)"
# Outcome: As expected.

person2 = Parent("Elizaveta", "Alekseeva")
# Prediction: Creates instance of Parent class with first name "Elizaveta" and last name "Alekseeva".
print(person2)
print(person2.first_name)
print(person2.last_name)
# Outcome: As expected.

print(person2.get_name())
# Prediction: Calls get_name method: "Elizaveta Alekseeva"
# Outcome: As expected.

# print(person2.get_full_name())
# Prediction: Parent instance has not access to Child methods, will error that there is no method of get_full_name.
# Outcome: AttributeError: 'Parent' object has no attribute 'get_full_name'

# person2.change_last_name("Tyurina")
# Prediction: Parent instance has not access to Child methods, will error that there is no method of change_last_name.
# Outcome: AttributeError: 'Parent' object has no attribute 'change_last_name'

print(person2.get_name())
# Prediction: Calls get_name method: "Elizaveta Alekseeva" as name has not changed due to inability to call change_last_name
# Outcome: As expected.

# print(person2.get_full_name())
# Prediction: Parent instance has not access to Child methods, will error that there is no method of get_full_name.
# Outcome: AttributeError: 'Parent' object has no attribute 'get_full_name'