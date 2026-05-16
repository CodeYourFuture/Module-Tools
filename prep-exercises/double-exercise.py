def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]


print(half(22))
print(half("hello"))
print(half("22"))


print(double(22))
print(double("hello"))
print(double("22"))

print(second(22))
print(second(0x16))
print(second("hello"))
print(second("22"))

# I expected the double("22"), my prediction was wrong, I expected that it will behave like javascript (smart enough to convert it to number but risky)
# however python will not change type to int and will just double the string ("2222"), because python is strongly typed.
