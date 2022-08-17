type_of_movie = input()
r = int(input())
c = int(input())

total_seats = r * c

ticket_price = 0

if type_of_movie == "Premiere":
    ticket_price = 12
elif type_of_movie == "Normal":
    ticket_price = 7.5
elif type_of_movie == "Discount":
    ticket_price = 5

total_income = total_seats * ticket_price
print(f"{total_income:.2f} leva")


