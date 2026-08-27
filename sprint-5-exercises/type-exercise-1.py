def half(value: int) -> float:
    return value / 2


def double(value: int) -> int:
    return value * 2


def second(value: int) -> int:
    return value[1]


print(half("22"))
print(double("22"))
print(second("22"))

# python throw the error after running the program, like "unsupported operand type";


# while type annotation give mypy tool to check the code before running the program and detects certain bugs;
"""
type-exercise-1.py:10: error: Value of type "int" is not indexable  [index]
type-exercise-1.py:13: error: Argument 1 to "half" has incompatible type "str"; expected "int"  [arg-type]
type-exercise-1.py:14: error: Argument 1 to "double" has incompatible type "str"; expected "int"  [arg-type]
type-exercise-1.py:15: error: Argument 1 to "second" has incompatible type "str"; expected "int"  [arg-type]

"""
