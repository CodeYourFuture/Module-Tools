# ------------------------
# Q. Predict what double("22") will do. Then run the code and check. Did it do what you expected? Why did it return the value it did?
# ------------------------

# A. I predicted that the return value of double("22") would be 44, because I know that in JavaScript '*' is a numeric operator and would coerce "22" into the number 22.
# It did not return what I expected and instead repeated the string twice, this is because in Python strings can be multiplied by integers to repeat them

# def double(value):
#     return value * 2


# print(double("22")) # Returns "2222"


# ------------------------
# Q. Read the above code and write down what the bug is. How would you fix it?
# ------------------------

# def double(number):
#     return number * 3

# print(double(10)) # Returns 30

# A. The bug is that the return value is triple the input value
# assuming the function is named correctly, it be can be fixed with this implemntation;

# def double(number):
#     return number * 2


# print(double(10)) # Returns 20
