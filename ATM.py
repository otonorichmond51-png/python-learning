balance = 100000
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
choice = int(input("choose option: "))
if choice == 1:
    print("Balance:", balance)
elif choice == 2:
    deposit_amount = float(input("Enter the amount to deposit: "))
    if deposit_amount <= 0:
        print("Invalid deposit amount.")
    else:
        balance += deposit_amount
        print("Deposit successful")
        print("New Balance:", balance)
elif choice == 3:
    withdraw_amount = float(input("Enter the amount to withdraw: "))
    if withdraw_amount <= 0:
        print("Invalid withdraw amount.")
    elif withdraw_amount > balance:
        print("Insufficient balance.")
    else:
        balance -= withdraw_amount
        print("Withdrawal successful")
        print("New Balance:", balance)
else:
    print("Invalid menu choice.")