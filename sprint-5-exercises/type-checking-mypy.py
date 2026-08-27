def open_account(balances: dict[str, int], name: str, amount: int) -> None:
    balances[name] = amount


def sum_balances(accounts: dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total


def format_pence_as_string(total_pence: int) -> str:
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = int(total_pence / 100)
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"


balances = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}

open_account(balances, "Tobi", 913)
open_account(balances, "Olya", 713)

total_pence = sum_balances(balances)
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")

# After running mypy tool then I found 3 errors as below:

# type-checking-mypy.py:27: error: Missing positional argument "amount" in call to "open_account"  [call-arg]
# type-checking-mypy.py:28: error: Missing positional argument "amount" in call to "open_account"  [call-arg]
# type-checking-mypy.py:31: error: Name "format_pence_as_str" is not defined  [name-defined]

# to fix the bug we need to add the positional argument in open account function and call the correct name of the second function. "format_pence_as_string"

# After adding type annotations to the functions and testing with mypy I got the following errors:
# sprint-5-exercises/type-checking-mypy.py:27: error: Argument 3 to "open_account" has incompatible type "float"; expected "int"  [arg-type].
# ========> To fix it, we should change the argument type from float to integer.

# sprint-5-exercises/type-checking-mypy.py:28: error: Argument 3 to "open_account" has incompatible type "str"; expected "int"  [arg-type]
# ==========> to fix this issue we should change the argument type from string to integer.
