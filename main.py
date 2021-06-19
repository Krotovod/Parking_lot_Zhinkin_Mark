import random
from transport import *
from parking_space import ParkingSpace
from parking_attendant import ParkingAttendant


if __name__ == '__main__':
    columns = random.randint(5, 10)
    rows = random.randint(3, 10)

    parking_place = [[ParkingSpace() for column in range(columns)] for row in range(rows)]
    for row in parking_place:
        random_size = random.randint(1, 3)
        for place in row:
            place.size = random_size

    # TODO Убрать! + добавить отображение текущего состояния стоянки
    for row in parking_place:
        print([(i.is_busy, i.size) for i in row])

    while True:
        new_transport = random.choice([Motorcycle(), Car(), Bus()])
        # TODO Добавить оповещение о новом транспорте
        ParkingAttendant().park_transport(parking_place, new_transport)
        # TODO Убрать! + добавить отображение текущего состояния стоянки
        for row in parking_place:
            print([(i.is_busy, i.size) for i in row])
        input()
        # TODO Оповещене о полной стоянке
