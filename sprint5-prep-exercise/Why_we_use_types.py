def double(value): return value * 2



def fix_double(value):
    return int(value) * 2

print(double("22"))
print(fix_double("22"))

#it returns "2222" -|> * works with string and it repeats it but "/" does not work with string
# fix_double returns 44 becouse we converted the string to number