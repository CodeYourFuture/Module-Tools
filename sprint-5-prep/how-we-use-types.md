```python
def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]

print(double(22))
print(double("hello"))
print(double("22"))
```
# Exercise 1:

Prediction:
double("22") will raise a typeError because "22" is a string.

Actual Result:
double ("22") actually returned "2222" so it actually resulted in a string repetition "2222"
this shows that the '*2' sign on strings will repeat them

# Exercise 2:

the bug on the code is the naming of the function. you can't call a function double() but then
the math is [value *3]. so we should either rename it triple() or change the method to [value *2]
depending on the context and what we are trying to achieve.