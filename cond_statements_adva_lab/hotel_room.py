month = input()
nights = int(input())

studio_night_price = 0
apartment_night_price = 0
discount_studio = 1
discount_apartment = 1

if month == "May" or month == "October":
    studio_night_price = 50
    apartment_night_price = 65
    if 7 < nights <= 14:
        discount_studio = 0.95
    elif nights > 14:
        discount_studio = 0.7

elif month == "June" or month == "September":
    studio_night_price = 75.20
    apartment_night_price = 68.70
    if nights > 14:
        discount_studio = 0.8

elif month == "July" or month == "August":
    studio_night_price = 76
    apartment_night_price = 77

if nights > 14:
    discount_apartment = 0.9

total_apartment_price = nights * (apartment_night_price * discount_apartment)
total_studio_price = nights * (studio_night_price * discount_studio)

print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")

