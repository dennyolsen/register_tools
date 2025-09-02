# REGISTER CLOSER for Community Cycles Bike Shop
# Author: Copyright (c) Dennis Olsen
# License: MIT

def get_total():
    print("CLOSE REGISTER\n" \
    # Twenties
    "$20 Bills Count:")
    twenties = int(input())
    total = twenties * 20
    print("Cash Total: $" + str (total) + "\n")

    # Tens
    print("$10 Bills Count:")
    tens = int(input())
    total = total + tens * 10
    print("Cash Total: $" + str (total) + "\n")

    # Fives
    print("$5 Bills Count:")
    fives = int(input())
    total = total + fives * 5
    print("Cash Total: $" + str (total) + "\n")

    # Ones
    print("$1 Bills Count:")
    ones = int(input())
    total = total + ones
    print("Cash Total: $" + str (total) + "\n")

    # Quarters
    print("Quarters Count:")
    quarters = int(input())
    total = total + quarters * .25
    print("Cash Total: $" + str (total) + "\n")

    # Dimes
    print("Dimes Count:")
    dimes = int(input())
    total = total + dimes * .1
    print("Cash Total: $" + str (total) + "\n")

    # Nickels
    print("Nickels Count:")
    nickels = int(input())
    total = total + nickels * .05
    print("Cash Total: $" + str (total) + "\n")

    # Pennies
    print("Pennies Count:")
    pennies = int(input())
    total = total + pennies * .01
    print("Cash Total: $" + str (total) + "\n")

    # Other
    print("Large bills and checks total")
    othermoney = float(input())
    total = total + othermoney
    print("Final Daily Total: $" + str (total) + "\n")

get_total()
