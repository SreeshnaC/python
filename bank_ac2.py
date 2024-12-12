
class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_account_details(self):
        print(f"\nAccount Number: {self.acc_no}")
        print(f"Account Holder Name: {self.name}")
        print(f"Account Type: {self.acc_type}")
        print(f"Balance: {self.balance}\n")


def menu():
    print("\nMenu:")
    print("1. Display Account Details")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


def main():

    account = BankAccount(101, "Sreeshna", "Savings", 30000)

    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            account.display_account_details()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
