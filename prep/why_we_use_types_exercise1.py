def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]


print(double("22"))

# Question
# Predict what double("22") will do. Then run the code and check. Did it do what you expected? Why did it return the value it did?

# Answer
# The function double("22") will return "2222".
# When I ran the program, it returned what I expected.
# The return value is "2222" because the argument is a string, so the * operator duplicates the string instead of 
# multiplying a number. Python repeats the string twice: "22" + "22" = "2222".