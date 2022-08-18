word = str(input())
total_points = 0

for ch in word:
    if ch == "a":
        total_points += 1
    elif ch == "e":
        total_points += 2
    elif ch == "i":
        total_points += 3
    elif ch == "o":
        total_points += 4
    elif ch == "u":
        total_points += 5

print(total_points)