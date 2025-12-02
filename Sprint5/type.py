def open_account(balances, name, amount): #dic type str and int
    balances[name] = amount

def sum_balances(accounts): #takes type dic[str, int}returns int
    total = 0
    for name, pence in accounts.items():
        print(f"{name} had balance {pence}")
        total += pence
    return total

def format_pence_as_string(total_pence): #type int returns type str
    if total_pence < 100:
        return f"{total_pence}p"
    pounds = int(total_pence / 100)
    pence = total_pence % 100
    return f"£{pounds}.{pence:02d}"

balances = {             #dic type {str:int}
    "Sima": 700,
    "Linn": 545,
    "Georg": 831,
}

open_account("Tobi", 9.13) # balances not passed, amount should be an int and not a float/ string
open_account("Olya", "£7.13")

total_pence = sum_balances(balances)  #returntype int
total_string = format_pence_as_str(total_pence) #returntype str and wrong function name 

print(f"The bank accounts total {total_string}")