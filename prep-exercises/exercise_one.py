
def double(value):
    return value * 2

print(double("22"))


# Predict what double("22") will do. Then run the code and check. Did it do what you expected? Why did it return the value it did?

# Initial prediction was that a type coercion may take place and  string "22"  will convert to integer 22 and thus the function returns 44.
# After running the code, I now know that it did not do what i expected. It duplicated/repeated the string and returned 2222.
