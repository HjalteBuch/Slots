money = 0
def deposit():
    global money
    while True:
        amount = input("How much do you want to deposit?: ")
        if(amount.isdigit() == False):
            print("You input was not recognized as a number")
            continue;

        amount = int(amount)

        if(amount <= 0):
            print("You have to deposit more than 0")
            continue;
        break;

    money += amount
    print("You now have " + str(money) + " DKK available to gamble away")


def play():
    print("playing")

deposit()

while True:
    match input("Would you like to gamble, deposit or leave: "):
        case "deposit":
            deposit()
        case "leave":
            quit
        case "gamble":
            play()
        case _:
            print("I didn't catch that")

