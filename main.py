from transport import *
from parking_space import *
from parking_attendant import ParkingAttendant
import time
import sys


if __name__ == '__main__':
    parking_attendant = ParkingAttendant()
    parking_lot, error_message = ParkingLot('user').create_parking_lot()
    if error_message != '':
        sys.exit(1)

    parking_attendant.parking_lot = parking_lot
    parking_attendant.show_parking_scheme()

    while True:
        new_transport = random.choice([Motorcycle(), Car(), Bus()])
        parking_attendant.park_transport(new_transport)
        parking_attendant.show_transports_list()
        parking_attendant.is_parking_full()
        parking_attendant.show_parking_scheme()
        time.sleep(2)
