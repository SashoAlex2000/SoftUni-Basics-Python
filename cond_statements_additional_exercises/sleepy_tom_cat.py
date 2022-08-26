from math import floor

holidays = int(input())

working_days = 365 - holidays
sum = holidays * 127 + working_days * 63

if sum > 30000:
    print("Tom will run away")
    print(f"{floor((sum - 30000) / 60)} hours and {(sum - 30000) % 60} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{floor(abs((sum - 30000) / 60))} hours and {abs((sum - 30000)) % 60} minutes less for play")
