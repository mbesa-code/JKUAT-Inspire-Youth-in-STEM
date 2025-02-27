enter_div_test = int(input("enter the divisibility test number"))
enter_number = int(input("enter a number: "))
if enter_number % enter_div_test == 0:
    print(enter_number,"is divisible by", enter_div_test)
else:
    print(enter_number,"is not divisible by", enter_div_test)