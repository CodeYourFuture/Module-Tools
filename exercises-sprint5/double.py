def double(value):
    return value * 2 


double("22")
print(double("22"))


# Coming from JS, I predicted that Python might behave the same way.
# Under the hood, without throwing an error, Python would concatenate
# the string "22" with itself, and the result would be "2222".

# correction: later on I realised JavaScript and Python behave differently JS coerces so "22" * 2 returns 44 in JS whereas Python repeats the string according to the number, so "22" * 2 returns "2222".


def double(number):
    return number * 3

print(double(10))

# As mentioned in prep section either the name should be triple or the code should be *2 