from typing import Dict

# Added Type Annotations
def open_account(balances: Dict[str, int], name: str, amount: int) -> None:
    balances[name] = amount

def sum_balances(accounts: Dict[str, int]) -> int:
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        # If 'pence' isn't an int, this will fail or cause issues later
        total += pence
    return total

def format_pence_as_string(total_pence: int) -> str:
    if total_pence < 100:
        return f"{total_pence}p"
    # Use // for floor division to ensure 'pounds' is an int
    pounds = total_pence // 100
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"

balances: Dict[str, int] = {
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}

# BUGS FIXED HERE: 
# Changed 9.13 (float) to 913 (int)
# Changed "£7.13" (str) to 713 (int)
open_account(balances, "Tobi", 913)
open_account(balances, "Olya", 713)

total_pence = sum_balances(balances)

# BUG FIXED HERE: Corrected the function name call
total_string = format_pence_as_string(total_pence)

print(f"The bank accounts total {total_string}")