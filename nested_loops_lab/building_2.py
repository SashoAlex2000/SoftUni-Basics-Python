floors = int(input())
rooms = int(input())

room_number = ""

for f in range(floors, 0 , -1):
    for r in range(rooms):
        current_number_of_room = f * 10 + r
        if f == floors:
            print(f"L{current_number_of_room} ", end = '')

        elif f % 2 != 0:
            room_number += f"A{current_number_of_room} "

        else:
            room_number += f'O{current_number_of_room} '

    print(room_number)
    room_number = ""
