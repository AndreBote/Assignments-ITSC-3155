# Andre Bautista
# 09/12/2025
# mbautis1@charlotte.edu
# ID: 801343013

### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}

# Coin values
DOLLAR = 1.00
HALF_DOLLAR = 0.50
QUARTER = 0.25
NICKEL = 0.05

### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, req_amount in ingredients.items():
            if self.machine_resources.get(item, 0) < req_amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item, req_amount in order_ingredients.items():
            self.machine_resources[item] -= req_amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


### Make an instance of SandwichMachine class and write the rest of the codes ###

# Prints out all current resources
def show_report(current_resources):
    print(f"Bread: {current_resources['bread']} slice(s)")
    print(f"Ham: {current_resources['ham']} slice(s)")
    print(f"Cheese: {current_resources['cheese']} pound(s)")


def main():
    # Make an instance of SandwichMachine
    machine = SandwichMachine(resources)

    # Input and code execution
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()
        if choice == "off":
            print("Thank you!")
            break

        if choice == "report":
            show_report(machine.machine_resources)
            continue

        if choice not in recipes:
            print(f"Sorry, '{choice}' is not a valid option.")
            continue

        order = recipes[choice]
        order_ingredients = order["ingredients"]
        cost = order["cost"]

        # Check resources
        if not machine.check_resources(order_ingredients):
            continue

        # Process coins and transaction
        coins_inserted = machine.process_coins()
        if not machine.transaction_result(coins_inserted, cost):
            continue

        # Make sandwich (deduct resources)
        machine.make_sandwich(choice, order_ingredients)


main()
print("Status 0")
