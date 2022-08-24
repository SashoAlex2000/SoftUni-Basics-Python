movie_title = input()
total_tickets_sold = 0
students_tickets = 0
standard_tickets = 0
kids_tickets = 0


while movie_title != "Finish":
    filled_seats = 0
    vacant_seats = int(input())
    while vacant_seats > filled_seats:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            students_tickets += 1
            filled_seats += 1
            total_tickets_sold += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            filled_seats += 1
            total_tickets_sold += 1
        elif ticket_type == "kid":
            kids_tickets += 1
            filled_seats += 1
            total_tickets_sold += 1
    print(f"{movie_title} - {filled_seats / vacant_seats * 100:.2f}% full.")

    movie_title = input()
    filled_seats = 0

print(f"Total tickets: {total_tickets_sold}")
print(f"{students_tickets / total_tickets_sold * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets_sold * 100:.2f}% standard tickets.")
print(f"{kids_tickets / total_tickets_sold * 100:.2f}% kids tickets.")
