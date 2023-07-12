class BankAccount:
    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance


def register():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    gender = input("Enter your gender: ")
    age = int(input("Enter your age: "))

    return BankAccount(name, surname, gender, age)


def login(accounts):
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    password = input("Enter your password: ")

    for account in accounts:
        if account.name == name and account.surname == surname:
            return account

    print("Account not found.")
    return None


def main():
    accounts = []

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account = register()
            accounts.append(account)
            print("Registration successful.")
        elif choice == '2':
            account = login(accounts)
            if account:
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
                    option = input("Enter your option: ")

                    if option == '1':
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                    elif option == '2':
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                    elif option == '3':
                        print(f"Current balance: {account.get_balance()}")
                    elif option == '4':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Login failed.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
