floors = int(input())
rooms = int(input())

for x1 in range(floors, 0, -1):
    for x2 in range(0, rooms):
        if x1 == floors:
            print(f"L{x1}{x2} ", end = '')

        elif x1 % 2 != 0:
            print(f"A{x1}{x2} ", end = '')
        elif x1 % 2 == 0:
            print(f"O{x1}{x2} ", end = '')

