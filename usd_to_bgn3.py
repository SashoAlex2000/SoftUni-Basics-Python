usd = float(input("Enter amount of money in USD: "))
exchange_rate = float(input("Enter the current day's exchange rate: "))

bgn = usd * exchange_rate
print(f'Today, {usd} amount of dollars is equal to {bgn} leva')
