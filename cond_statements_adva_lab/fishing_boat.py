budget = int(input())
season = input()
fishermen = int(input())

rent = 0
discount = 0
even_discount = 0

if season == "Spring":
    rent = 3000
elif season == "Summer":
    rent = 4200
elif season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600


if fishermen <= 6:
        discount = 0.1
elif 6 < fishermen <= 11:
        discount = 0.15
elif fishermen > 11:
        discount = 0.25


if season != "Autumn" and fishermen % 2 == 0:
    even_discount = 0.05

final_rent = (rent * (1 - discount)) * (1 - even_discount)

difference = budget - final_rent
if difference >= 0:
    print(f"Yes! You have {difference:.2f} leva left.")
if difference < 0:
    print(f"Not enough money! You need {abs(difference):.2f} leva.")

#pri AND i OR trqbva skobi da se polzvat za da se spokaje koe se ima predvid
