def open_account(balances: dict, name: str, amount: int) -> None:
    balances[name] = amount

def sum_balances(accounts: dict) -> int:
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




# When I ran mypy I got these errors:

# Error 1: bank.py:24: error: Missing positional argument "amount" in call to "open_account" [call-arg]
# The function open_account expects three arguments but only two have been passed. We need to add one more argument.

# Error 2: Argument 1 has incompatible type "str"; expected "dict"
# By adding balances as the first argument, this will be solved as well.

# Error 3: Argument 2 has incompatible type "float"; expected "str"
# 9.13 is in the wrong position, and it's a float not an int.

# Error 4: Missing positional argument "amount" in call to "open_account"
# Same problem as Error 1 missing balances and wrong types.

# Error 5: bank.py:25: error: Argument 1 to "open_account" has incompatible type "str"; expected "dict[Any, Any]"
# Line 25 has two bugs: balances should be passed as the first argument, and the third argument is passed as a string which should be an int.

# Error 6: bank.py:28: error: Name "format_pence_as_str" is not defined [name-defined]
# Typo! Should be format_pence_as_string.