# NAME: KADE BRENDA RAMBA
# REG.NO: S26B38/050
# THIS PROGRAM PROCESSES CITYLINK MINI-BANK CUSTOMER ACCOUNT APPLICATIONS,
#
# ask how many customers will be processed
number_of_customers = int(input("How many customers?"))

accounts_opened = 0
total_deposited = 0

# process each customer 
for customer in range(1, number_of_customers + 1):
    print("--- Customer",customer, "---")

# customers information
name = input("Name: ") 
age = int(input("Age: "))   
account_type =input("Account_type(S/C/T): ").upper()

#function to check whether a customer is eligible,to open a selected account type
def check_eligibility(age, account_type):
    """Return True if the customer qualifies for the selected account."""
    if account_type == "S":
       return True
    elif account_type == "C":
        return True
    elif account_type == "T":
        if age <= 25:
            return True
        else:
            return False
    else:
        return False
    
# Eligibility of the customer
if account_type not in ("S","C","T"):
    print("Invalid account type. Please choose S, C or T")
if not check_eligibility(age,account_type):
    if account_type =="T":
       print("Sorry, Student accounts are only for age 25 or below.")

def get_minimum_deposit(account_type):
        """Return the minimum deposit for the selected account type."""
        if account_type == "S":
            return 50000
        elif account_type== "C":
            return 100000
        elif account_type == "T":
            return 20000
        else:
            return 0    

# deposit
minimum = get_minimum_deposit(account_type)
deposit = float(input("Initial deposit: "))
if deposit >= minimum:
    print("Account opened successfully for", name, ".Balance:", deposit, "UGX")
    if account_type == "S":
        account_name = "Savings"
    elif account_type == "C":
        account_name = "Current"
    else:
        account_name = "Student"

        accounts_opened += 1
        total_deposited += deposit 
    print("Account opened successfully for", name, "UGX")
else:
    print("Deposit too low. Minimum for this account is",deposit,"UGX.")
   

# final summary
print("===== SESSION SUMMARY=====")
print("Accounts opened:", accounts_opened)
print("Total deposited:", total_deposited,"UGX")

    