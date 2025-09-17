from savings_account import SavingsAccount
from checking_account import CheckingAccount


def main():
    print("=== Savings Accounts ===")
    s1 = SavingsAccount("Seth", 1000, 100, "SA123", "RN001", 0.05)
    s2 = SavingsAccount("Jane", 2000, 200, "SA456", "RN002", 0.03)
    s1.print_customer_information()
    s1.apply_interest()
    s1.print_customer_information()

    s2.print_customer_information()
    s2.apply_interest()
    s2.print_customer_information()

    print("=== Checking Accounts ===")
    c1 = CheckingAccount("Seth", 1000, 100, "SA123", "RN003", 1000)
    c2 = CheckingAccount("Jane", 2000, 200, "SA456", "RN004", 1000)

    c1.print_customer_information()
    c2.print_customer_information()

    print("Test: Seth transfers $400 to Jane")
    c1.transfer(400, c2)

    c1.print_customer_information()
    c2.print_customer_information()

    print("Test: Jane withdraws $200")
    c2.withdraw(200)

    c2.print_customer_information()


main()
