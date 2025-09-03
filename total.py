from moneyed import Money

def close_register():
    total = Money(0.00, 'USD')

    hundreds = Money(int(input("How many $100 bills?\n")) * 100.00, 'USD')
    print(hundreds)
    total = total + hundreds

    fifties = Money(int(input("How many $50 bills?\n")) * 50.00, 'USD')
    print(fifties)
    total = total + fifties

    twenties = Money(int(input("How many $20 bills?\n")) * 20.00, 'USD')
    print(twenties)
    total = total + twenties

    tens = Money(int(input("How many $10 bills?\n")) * 10.00, 'USD')
    print(tens)
    total = total + tens

    fives = Money(int(input("How many $5 bills?\n")) * 5.00, 'USD')
    print(fives)
    total = total + fives

    ones = Money(int(input("How many $1 bills?\n")) * 1.00, 'USD')
    print(ones)
    total = total + ones

    quarters = Money(int(input("How many quarters?\n")) * 0.25, 'USD')
    print(quarters)
    total = total + quarters

    dimes = Money(int(input("How many dimes?\n")) * 0.10, 'USD')
    print(dimes)
    total = total + dimes

    nickels = Money(int(input("How many nickels?\n")) * 0.05, 'USD')
    print(nickels)
    total = total + nickels

    pennies = Money(int(input("How many pennies?\n")) * 0.01, 'USD')
    print(pennies)
    total = total + pennies

    return total

print("\nTotal: " + str(close_register()))

