number = int(input())

for num in range(0, number + 1, 2):
    print(2 ** num)

# OR
# for num in range(number + 1):
#     if num % 2 == 0:
#         print(2**num)