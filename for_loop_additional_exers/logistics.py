number_of_cargoes = int(input())
microbus_tons = 0
truck_tons = 0
train_tons = 0

for i in range(number_of_cargoes):
    tons = int(input())

    if tons <= 3:
        microbus_tons += tons
    elif 4 <= tons <= 11:
        truck_tons += tons
    else:
        train_tons += tons

total_tons = microbus_tons + truck_tons + train_tons

microbus_price = microbus_tons * 200
truck_price = truck_tons * 175
train_price = train_tons * 120

average_price = (microbus_price + train_price + truck_price) / total_tons

print(f"{average_price:.2f}")
print(f"{microbus_tons / total_tons * 100:.2f}%")
print(f"{truck_tons / total_tons * 100:.2f}%")
print(f"{train_tons / total_tons * 100:.2f}%")