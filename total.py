# Community Cycles Register Closer
# Author: Dennis Olsen
# License: MIT

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

def total_checks():
    print("Totaling checks...")
    checkscheck = input('Do you have checks? (y/n): ').lower().startswith('y')
    checkstotal = Money(0.00, 'USD')
    if checkscheck == True:
        checksnumber = int(input("How many checks do you have? "))
        # print(checksnumber)
        for check in range(checksnumber):
            print("Check Number " + str(check + 1) + " Total: ")
            amount = Money(input(), 'USD')
            checkstotal = checkstotal + amount
        # checkstotal = Money(3.50, 'USD')
    else:
        checkstotal = Money(0.00, 'USD')

    return checkstotal
    

register_count = close_register()

checkstotal = total_checks()

print("\nCash Count: " + str(register_count))
print("\nChecks Count: " + str(checkstotal))

daily_total = register_count + checkstotal

print("\nDaily Register Total: " + str(daily_total))
