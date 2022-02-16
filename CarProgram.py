import CarClass as c

Kia = c.Car(2020, "California")

for i in range(1, 6):
    Kia.accelerate()
    print("The car is moving", Kia.get_speed(), "mph")

print()

for j in range(1, 6):
    Kia.brake()
    print("The car is moving", Kia.get_speed(), "mph")