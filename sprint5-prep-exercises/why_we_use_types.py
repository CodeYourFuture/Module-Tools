"""Examples from the "Why we use types" section.

This file demonstrates why type checking matters.
The `double()` example behaves surprisingly when given a string.
"""


def half(value):
    return value / 2


def double(value):
    return value * 2


def second(value):
    return value[1]


def safe_run(func, arg):
    try:
        result = func(arg)
    except Exception as e:
        print(f"{func.__name__}({arg!r}) -> ERROR: {e}")
    else:
        print(f"{func.__name__}({arg!r}) -> {result!r}")


if __name__ == '__main__':
    safe_run(half, 22)
    safe_run(half, "hello")
    safe_run(half, "22")
    safe_run(double, 22)
    safe_run(double, "hello")
    safe_run(double, "22")
    safe_run(second, 22)
    safe_run(second, 0x16)
    safe_run(second, "hello")
    safe_run(second, "22")

# Answers to the prep exercises
# 1) Predict what `double("22")` will do. Then run the code and check.
#    - Prediction: calling `double("22")` will repeat the string, returning "2222".
#    - Reason: In Python, multiplying a string by an integer repeats the string.
#    - Confirmed by running this script: `double('22') -> '2222'`.

# 2) Read the above code and write down what the bug is. How would you fix it?
#    - Bug: the example discussed in the curriculum shows `double(number)` implemented
#      incorrectly as `return number * 3`, which triples instead of doubles.
#    - Fix: change the implementation to `return number * 2` (or rename the function
#      to `triple()` if the intention was to multiply by 3).
#    - Note: this is a logic bug (not a type error), so type checkers would not catch it.
