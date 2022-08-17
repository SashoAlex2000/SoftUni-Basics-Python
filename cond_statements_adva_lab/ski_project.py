days = int(input())
type_of_room = input()
review = input()
nights = days - 1

price_per_night = 0
discount = 1

if type_of_room == "room for one person":
    price_per_night = 18
    discount = 1

elif type_of_room == "apartment":
    price_per_night = 25
    if nights < 10:
        discount = 0.7
    elif nights <= 15:
        discount = 0.65
    elif nights > 15:
        discount = 0.5

elif type_of_room == "president apartment":
    price_per_night = 35
    if nights < 10:
        discount = 0.9
    elif nights <= 15:
        discount = 0.85
    elif nights > 15:
        discount = 0.8

total_price = (nights * price_per_night) * discount

if review == "positive":
    total_price *= 1.25
elif review == "negative":
    total_price *= 0.9

print(f"{total_price:.2f}")

