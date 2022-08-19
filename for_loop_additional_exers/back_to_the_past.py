inheritance = float(input())
death_year = int(input())

is_money_over = False

for year in range(1800, death_year + 1):
    if year % 2 == 0:
        spent_money = 12000
        inheritance -= spent_money
    elif year % 2 != 0:
        spent_money = 12000 + 50 * (year - 1800 + 18)
        inheritance -= spent_money


if inheritance < 0:
    is_money_over = True

if is_money_over == False:
    print(f"Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.")
else:
    print(f"He will need {abs(inheritance):.2f} dollars to survive.")

