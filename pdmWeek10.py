# menu dictionary - shows items and prices
menu = {"coca cola": 2.10, "pepsi":2.24, "fiji water":1.93, "sprite": 2.12}
# stock dictionary - shows items and stocks
stock = {"coca cola": 10,  "pepsi":10, "fiji water":10, "sprite": 10 }

# order dictionary - shows customer ordered items and quantitty
order = {} 
# addOrder - boolean value for keep adding order 
addOrder = True


# display menu with iteration
print ("MENU")
for key,value in menu.items():
    print()
    print(key,': ${:.2f}'.format(value))
    

while (addOrder == True):
    # input product to order with validation
    _order_ = input("what would you like to order? ").strip().lower()
    while _order_ not in menu:
        _order_ = input("what would you like to order? ").strip().lower()
   
    # add order with validation
    _qtty_ = 0 
    while (_qtty_ <=0):
        _qtty_ = int(input("quantity: "))
     
    # check for stock availability
    if _qtty_ > stock[_order_]:
        print("item is out of stock")
    else:
        order[_order_] = _qtty_
        stock[_order_] -= _qtty_

    # add another order?
    addOrder = input("add order? (y/n): ")
    if (addOrder.strip().lower() == "n"):
        addOrder = False
    else: 
        addOrder= True
        
print(order) # {'pepsi':2, 'cocacola':2}



# calculating total amount
_ttl_ = 0
for key in order.keys():
    _ttl_ += (menu[key]*order[key])

# output ttl amount 
print("your total is ${:.2f}".format(_ttl_))


# printing reciept
print()
print('------------RECIEPT--------------')
for key,value in order.items():
    print(key, end="                  ")
    print(value, end="  ")
    print('${:.2f}'.format(menu[key]))
print()
print("your total is               ${:.2f}".format(_ttl_))
print('---------------------------------')


# enter payment and validate value
payment = eval(input("payment: $"))
while (payment<_ttl_):
    print("not enough balance")
    payment = eval(input("payment: $"))

# calculate change 
change = payment - _ttl_ 

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
print("")
print("CHANGE")
if (pennies>0):
    print ("pennies: ", pennies)
if (quarters>0):
    print ("quarters: ", quarters)
if (nickels>0):
    print ("nickels: ", nickels)
if (dimes>0):
    print ("dimes: ", dimes)



