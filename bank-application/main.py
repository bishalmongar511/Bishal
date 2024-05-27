from account_manager import create_account, login, delete_account, load_accounts, update_accounts_file

def main():
    accounts = load_accounts()  # Load accounts at the start
    while True:
        print("Welcome to Terminal Bank!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print("Choose account type:")
            print("1. Personal")
            print("2. Business")
            account_type_choice = input("Enter 1 or 2: ")
            account_type = 'Personal' if account_type_choice == '1' else 'Business' if account_type_choice == '2' else None
            if account_type:
                account_number, password = create_account(account_type)
                print(f"Account created successfully! Your account number is {account_number} and your password is {password}")
            else:
                print("Invalid account type!")

        elif choice == '2':
            account_number = input("Enter account number: ")
            password = input("Enter password: ")
            account = login(account_number, password)
            if account:
                while True:
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. Delete Account")
                    print("6. Logout")
                    choice = input("Choose an option: ")

                    if choice == '1':
                        print(f"Your balance is: {account.balance}")

                    elif choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        if account.deposit(amount):
                            print("Deposit successful!")
                            accounts[account.account_number] = account
                            update_accounts_file(accounts)
                        else:
                            print("Invalid amount!")

                    elif choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        if account.withdraw(amount):
                            print("Withdrawal successful!")
                            accounts[account.account_number] = account
                            update_accounts_file(accounts)
                        else:
                            print("Insufficient funds or invalid amount!")

                    elif choice == '4':
                        target_account_number = input("Enter target account number: ")
                        amount = float(input("Enter amount to transfer: "))
                        target_account = accounts.get(target_account_number)
                        if target_account and account.transfer(target_account, amount):
                            print("Transfer successful!")
                            accounts[account.account_number] = account
                            accounts[target_account.account_number] = target_account
                            update_accounts_file(accounts)
                        else:
                            print("Transfer failed! Check account details and balance.")

                    elif choice == '5':
                        if delete_account(account.account_number):
                            print("Account deleted successfully!")
                            break
                        else:
                            print("Account deletion failed!")

                    elif choice == '6':
                        print("Logged out successfully!")
                        break

                    else:
                        print("Invalid option!")
            else:
                print("Invalid account number or password!")

        elif choice == '3':
            print("Thank you for using Terminal Bank! Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
