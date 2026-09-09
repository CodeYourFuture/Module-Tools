def open_account(balances, name, amount):
    balances[name] = amount

def sum_balances(accounts):
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence):
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

open_account("Tobi", 9.13)
open_account("Olya", "£7.13")

total_pence = sum_balances(balances)
total_string = format_pence_as_str(total_pence)

print(f"The bank accounts total {total_string}")

# TASK
# This code contains bugs related to types. They are bugs mypy can catch.
#
# 1. Read this code to understand what it's trying to do.
# 2. Install and set up mypy in a python virtual environment
# 3. Add type annotations everywhere appropriate
# 4. Run `mypy 04-addmypy.py`, and fix any errors
# 5. When you're confident all of the type annotations are correct, and the bugs are fixed, run the code and check it works.
