import time

# Display message prompting the user to enter their card
print("Please Enter Your CARD")

# Simulate a delay of 5 seconds to mimic card reading process
time.sleep(5)

# Define the ATM PIN and initial balance
password = 8008
balance = 5000

# Transaction history list to store tuples of (transaction_type, amount)
transaction_history = []

# Prompt the user to enter their ATM PIN
pin = int(input("Enter your ATM Pin: "))

# Check if the entered PIN matches the predefined password
if pin == password:
    # If PIN is correct, enter into an infinite loop for ATM operations
    while True:
        # Display the menu of options for the user
        print("""
             1 == Check Balance
             2 == Withdraw Cash
             3 == Deposit Cash
             4 == Transaction History
             5 == Change PIN
             6 == Exit
             """)

        try:
            # Prompt the user to enter their choice and convert it to integer
            option = int(input("Please Enter Your choice(1-6):"))
        except ValueError:
            # Handle the case where non-integer input is provided
            print("Please Enter Valid Option")

        # Option 1: Check Balance
        if option == 1:
            print("=========================================================")
            print(f"Your current balance is {balance}")
            print("=========================================================")

        # Option 2: Withdraw Balance
        elif option == 2:
            # Prompt the user to enter the amount to withdraw
            withdraw_amount = int(input("Please Enter Withdraw amount: "))
            # Check if there is sufficient balance for withdrawal
            if withdraw_amount > balance:
                print("Insufficient balance")
            else:
                # Deduct the withdrawal amount from the balance
                balance -= withdraw_amount
                # Add the transaction to history
                transaction_history.append(("Withdrawal", withdraw_amount))
                print("=========================================================")
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your Current Balance is {balance}")
                print("=========================================================")

        # Option 3: Deposit Balance
        elif option == 3:
            # Prompt the user to enter the amount to deposit
            deposit_amount = int(input("Please Enter Deposit amount: "))
            # Add the deposit amount to the balance
            balance += deposit_amount
            # Add the transaction to history
            transaction_history.append(("Deposit", deposit_amount))
            print("=========================================================")
            print(f"{deposit_amount} is credited to Your Account")
            print(f"Your Current Balance is {balance}")
            print("=========================================================")

        # Option 4: Transaction History
        elif option == 4:
            print("=========================================================")
            print("Transaction History:")
            for transaction in transaction_history:
                transaction_type, amount = transaction
                print(f"{transaction_type}: {amount}")
            print("=========================================================")

        # Change PIN
        elif option == 5:
            new_pin = input("Enter new PIN: ")
            pin = new_pin
            print("PIN changed successfully.")

        # Option 5: Exit
        elif option == 6:
            # Print a thank you message and break out of the loop to exit the program
            print("THANK YOU")
            break

else:
    # If the entered PIN does not match the predefined password, notify the user
    print("Wrong Pin. Please try again")
