from math import floor

number_of_tournaments = int(input())
starting_points = int(input())

points_won = 0
tournaments_won = 0

for i in range(number_of_tournaments):
    current_tournament = input()
    if current_tournament == "W":
        points_won += 2000
        tournaments_won += 1
    elif current_tournament == "F":
        points_won += 1200
    elif current_tournament == "SF":
        points_won += 720

final_points = starting_points + points_won
average_points = points_won / number_of_tournaments
percentage_tournaments_won = tournaments_won / number_of_tournaments * 100
average_points = floor(average_points)

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percentage_tournaments_won:.2f}%")
