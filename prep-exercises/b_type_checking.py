# ------------------------
# Exercise 1
# ------------------------
# Read the code to understand what it’s trying to do. 
# Add type annotations to the method parameters and return types of this code. 
# Run the code through mypy, and fix all of the bugs that show up. 
# When you’re confident all of the type annotations are correct, and the bugs are fixed, run the code and check it works.



# added type annotations to balances of dictionary[string, integer] to represent the structure needed, string to name and integer to amount, 
# with the return type of none (as there is nothing to return)
def open_account(balances: dict[str, int], name: str, amount: int) -> None:
    balances[name] = amount

# added type annotation of dictionary to the accounts argument because it reflects the balances argument,
# and a return type of integer.
def sum_balances(accounts: dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

# added integer type annotation and a return type of string for the output
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

# added the balances dictionary as first argument (as required above)
# and altered the amounts types from float 9.13 and string "7.13" to integers
open_account(balances, "Tobi", 913)
open_account(balances, "Olya", 713)

total_pence = sum_balances(balances)
# corrected the function name (originally was "format_pence_as_str")
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")