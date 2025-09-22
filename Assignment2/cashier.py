DOLLAR = 1.00
HALF_DOLLAR = 0.50
QUARTER = 0.25
NICKEL = 0.05

class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        try:
            large_dollars = int(input("how many large dollars?: ").strip() or "0")
            half_dollars = int(input("how many half dollars?: ").strip() or "0")
            quarters = int(input("how many quarters?: ").strip() or "0")
            nickels = int(input("how many nickels?: ").strip() or "0")
        except ValueError:
            # Error case for non-integers
            print("Sorry, only numbers are allowed.")
            large_dollars = half_dollars = quarters = nickels = 0

        total = (
                large_dollars * DOLLAR +
                half_dollars * HALF_DOLLAR +
                quarters * QUARTER +
                nickels * NICKEL
        )
        return round(total, 2)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print(f"Sorry that's not enough money. Money refunded.")
            return False
        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
        return True