def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]

print(double("22"))

# My prediction is that double("22") will return 44
# When running the code, it did not return what I expected. instead, the output is '2222'
# It returned '2222' because the input ( 22 ) is a text not a number