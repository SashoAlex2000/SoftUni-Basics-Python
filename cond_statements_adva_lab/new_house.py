type_of_flower = input()
quantity = int(input())
budget = int(input())

price = 0
discount = 1

if type_of_flower == "Roses":
    price = 5
    if quantity > 80:
        discount = 0.9

elif type_of_flower == "Dahlias":
    price = 3.8
    if quantity > 90:
        discount = 0.85

elif type_of_flower == "Tulips":
    price = 2.8
    if quantity > 80:
        discount = 0.85

elif type_of_flower == "Narcissus":
    price = 3
    if quantity < 120:
        discount = 1.15

elif type_of_flower == "Gladiolus":
    price = 2.5
    if quantity < 80:
        discount = 1.2

total_price = (quantity * price) * discount
difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {quantity} {type_of_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")


