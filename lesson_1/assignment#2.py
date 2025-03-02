
enter_temperature = int(input("enter the temperutere : "))
if enter_temperature >= 30:
    print("It's too hot! Stay hydrated")
elif 20 <= enter_temperature < 30:
    print("The weather is pleasant")
elif 10 <= enter_temperature < 20:
    print("It's a bit chilly. Wear a sweater")
else:
    print("It's very cold! Wear a jacket")


    