import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


# Prints out all current resources
def show_report(current_resources):
    print(f"Bread: {current_resources['bread']} slice(s)")
    print(f"Ham: {current_resources['ham']} slice(s)")
    print(f"Cheese: {current_resources['cheese']} pound(s)")


def main():
    ###  write the rest of the codes ###
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()
        if choice == "off":
            print("Thank you!")
            break

        if choice == "report":
            show_report(sandwich_maker_instance.machine_resources)
            continue

        if choice not in recipes:
            print(f"Sorry, '{choice}' is not a valid option.")
            continue

        order = recipes[choice]
        order_ingredients = order["ingredients"]
        cost = order["cost"]

        # Check resources
        if not sandwich_maker_instance.check_resources(order_ingredients):
            continue

        # Process coins and transaction
        coins_inserted = cashier_instance.process_coins()
        if not cashier_instance.transaction_result(coins_inserted, cost):
            continue

        # Make sandwich (deduct resources)
        sandwich_maker_instance.make_sandwich(choice, order_ingredients)


if __name__ == "__main__":
    main()
