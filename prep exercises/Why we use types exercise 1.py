def double(value):
    return value * 2

# I predict that double("22") will produce 22.0

result = double("22")
print(result) # Actual result is 2222

# This is because the string is duplicated twice, "22" + "22" = "22" * 2, it is repeating the a sequence of string.
