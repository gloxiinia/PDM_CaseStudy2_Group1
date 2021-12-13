# asks for amount of change that is non negative
change = 0
while (change < 0):
    change = float(input("change owed: $"))


# converting to cents
cents = round(change * 100);


# checks for 25c
quarters = 0
while (cents >= 25):

    cents = cents -  25
    quarters+=1


# checks for 10 cents
dimes = 0;
while (cents >= 10):
    cents = cents - 10;
    dimes=+1




# checks for 5c
nickels = 0;
while (cents >= 5):
    cents = cents - 5;
    nickels+=1;


# checks for $0.01
pennies = 0;
while (cents >= 1):
    cents = cents - 1;
    pennies+=1;


# displays output
print("least number of coins: ", pennies+quarters+nickels+dimes)