

type_of_fuel = input()
fuel_in_tank = float(input())

x = ["Diesel","Gasoline","Gas"]


if type_of_fuel not in x:
    print("Invalid fuel!")
    exit()
else:
    pass

type_of_fuel = type_of_fuel.lower()

if fuel_in_tank >= 25:
    print(f"You have enough {type_of_fuel}.")
else:
    print(f"Fill your tank with {type_of_fuel}!")

