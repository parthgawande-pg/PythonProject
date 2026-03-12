# Initial balance
balance = 0

# Functions
def display_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount deposited successfully.")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful.")
    else:
        print("Insufficient balance!")

# Menu driven program
while True:
    print("\n--- BANK MENU ---")
    print("1. Display Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank you!")
        break

    if choice == 1:
        display_balance()

    elif choice == 2:
        amt = int(input("Enter amount to deposit: "))
        deposit(amt)

    elif choice == 3:
        amt = int(input("Enter amount to withdraw: "))
        withdraw(amt)

    else:
        print("Invalid choice!")