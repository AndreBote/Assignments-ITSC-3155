class BankAccount:
    bank_title = "Python Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print("Deposited " + str(amount) + "\n")
        else:
            print("Deposit amount must be greater than zero.\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be greater than zero.\n")
        elif self.current_balance - amount < self.minimum_balance:
            print("Withdrawal canceled. Current balance would fall below minimum balance.\n")
        else:
            self.current_balance -= amount
            print("Withdrew " + str(amount) + "\n")

    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.__routing_number}\n")


# # First
# print("First Instance:")
# print("-" * 30)
#
# account1 = BankAccount("Yanagi", 300, 50)
# account1.print_customer_information()
# account1.deposit(0)  # should fail
# account1.deposit(200)
# account1.print_customer_information()
# account1.withdraw(100)
# account1.print_customer_information()
#
# # Second
# print("Second Instance:")
# print("-" * 30)
#
# account2 = BankAccount("Miyabi", 2000, 100)
# account2.print_customer_information()
# account2.deposit(500)
# account2.print_customer_information()
# account2.withdraw(2450)  # should fail
# account2.withdraw(200)   # should succeed
# account2.print_customer_information()