
def do_everything(x,y):
    while True:
        print("What function do you want to do? 1: Addition, 2: Subtraction, a: Quick Chat, l: leave")
        user_choice = input()

        if user_choice == "a":
            useless_chat()
        elif user_choice == "1":
            print(addition(x,y))
        elif user_choice == "2":
            print(subtraction(x,y))
        elif user_choice == "l":
            break
        else:
            print("Invalid choice")

    print("Thank you for using BadCalculator")


# Takes 2 user inputs if inputs match the if statements, returns the specified amount. If any user input is greater than 5 or not a number, will return error message
def addition(x, y):
    x = int(input("Enter the first number (up to 5) : "))
    y = int(input("Enter the second number (up to 5) : "))
    if ((x == 1 and y == 0) or (x == 0 and y == 1)):
        total = 1
        return total
    elif ((x == 2 and y == 0) or (x == 0 and y == 2)):
        total = 2
        return total
    elif ((x == 3 and y == 0) or (x == 0 and y == 3)):
        total = 3
        return total
    elif ((x == 4 and y == 0) or (x == 0 and y == 4 )):
        total = 4
        return total
    elif ((x == 5 and y == 0) or (x == 0 and y == 5)):
        total = 5
        return total
    elif (x == 0 and y == 0):
        total = 0
        return total
    elif (x == 1 and y == 1):
        total = 2
        return total
    elif ((x == 1 and y == 2) or (x == 2 and y == 1)):
        total = 3
        return total
    elif ((x == 1 and y == 3) or (x == 3 and y == 1)):
        total = 4
        return total
    elif ((x == 1 and y == 4) or (x == 4 and y == 1)):
        total = 5
        return total
    elif ((x == 1 and y == 5) or (x == 2 and y == 5)):
        total = 6
        return total
    elif (x == 2 and y == 2):
        total = 4
        return total
    elif ((x == 2 and y == 3) or (x == 3 and y == 2)):
        total = 5
        return total
    elif ((x == 2 and y == 4) or (x == 4 and y == 2)):
        total = 6
        return total
    elif ((x == 2 and y == 5) or (x == 5 and y == 2)):
        total = 7
        return total
    elif (x == 3 and y == 3):
        total = 6
        return total
    elif ((x == 3 and y == 4) or (x == 4 and y == 3)):
        total = 7
        return total
    elif ((x == 3 and y == 5) or (x == 5 and y == 3)):
        total = 8
        return total
    elif (x == 4 and y == 4):
        total = 8
        return total
    elif ((x == 4 and y == 5) or (x == 5 and y == 4)):
        total = 9
        return total
    elif (x == 5 and y == 5):
        total = 10
        return total
    else:
        return ("Invalid input!")

def subtraction(x,y):
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    return x - y

    # I had a pandan waffle today


# A useless function where user can tell calculator how they are doing and no matter what the user says, program responds with "Cool!"
def useless_chat():
    while True:
        response= input("Hello, whats on your mind? ('stop' to exit)")
        if response == "stop" :
            break

def main():
    print("Welcome to Calc! input 2 numbers ")
    x = input()
    y = input()
    do_everything(x, y)

main()
