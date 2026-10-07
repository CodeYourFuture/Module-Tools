# ✍️exercise
# Predict what double("22") will do. Then run the code and check.
#  Did it do what you expected? no
#  Why did it return the value it did? it just concatenated (repeated) the string. I expected it returns 44, but there is type issue.


def double(value):
    return value * 2 

print(double("22"))

# ---------------
def double(number):
    return number * 3

print(double(10))

# ✍️exercise
# Read the above code and write down what the bug is. How would you fix it?
# it will return 30, but the function name is double, so we have to change the function name to triple or change the return statement to number * 2. 

