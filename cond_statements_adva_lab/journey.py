budget = float(input())
season = input()
money_spent = 0
residence = ""
country = ""

if budget <= 100:
    country = "Bulgaria"
    if season == "summer":
        money_spent = 0.3 * budget
        residence = "Camp"
    elif season == "winter":
        money_spent = 0.7 * budget
        residence = "Hotel"

elif budget <=1000:
    country = "Balkans"
    if season == "summer":
        money_spent = 0.4 * budget
        residence = "Camp"
    elif season == "winter":
        money_spent = 0.8 * budget
        residence = "Hotel"

elif budget > 1000:
    country = "Europe"
    money_spent = 0.9 * budget
    residence = "Hotel"

print(f"Somewhere in {country}")
print(f"{residence} - {money_spent:.2f}")

