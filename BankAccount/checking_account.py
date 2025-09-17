from bank_account import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, target_account):
        if amount > self.transfer_limit:
            print(f"Transfer failed. Limit is {self.transfer_limit}.\n")
        elif self.current_balance - amount < self.minimum_balance:
            print(f"Transfer failed. Balance would fall below minimum balance.\n")
        else:
            self.current_balance -= amount
            target_account.current_balance += amount
            print(f"Transfer successful. {self.customer_name}'s balance is {self.current_balance}.")
            print(f"{target_account.customer_name}'s balance is {target_account.current_balance}.\n")



