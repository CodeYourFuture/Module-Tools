
from typing import Dict
def open_account(balances: Dict[str,int], name:str, amount:int): #dic type str and int
    #Adding a new account 
    balances[name] = amount

def sum_balances(accounts:Dict[str,int])-> int: #takes type dic[str, int}returns int
    total = int = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence: int)-> str: #type int returns type str
    #formatting pence as a string 
    if total_pence < 100:
        return f"{total_pence}p"
    pounds =int(total_pence / 100)
    reveal_type(pounds)  
    pence = total_pence % 100
    reveal_type(pence)
    return f"£{pounds}.{pence:02d}"

balances:Dict[str,int]  = {             #dic type {str:int}
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}

open_account("Tobi", 9.13) # balances not passed, amount should be an int and not a float/ string
open_account("Olya", "£7.13")

total_pence = sum_balances(balances)  #returntype int
reveal_type(total_pence)
total_string = format_pence_as_str(total_pence) #returntype str and wrong function name
reveal_type(total_string)
print(f"The bank accounts total {total_string}")