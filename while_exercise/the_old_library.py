favourite_book = input()

book = ""
book_counter = 0
is_book_found = False

while True:
    book = input()
    if book != favourite_book:
        book_counter += 1

    elif book == favourite_book:
        is_book_found = True
        break

    if book == "No More Books":
        is_book_found = False
        break

if is_book_found == True:
    print(f"You checked {book_counter} books and found it.")

elif is_book_found == False:
    print("The book you search is not here!")
    print(f"You checked {book_counter - 1} books.")

