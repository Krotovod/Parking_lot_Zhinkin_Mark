import logging

import random
import config

file_log = logging.FileHandler('Log.log')
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out),
                    format='[%(asctime)s | %(levelname)s]: %(message)s',
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)


class ParkingSpace:

    def __init__(self, size=0):
        self.size = size
        self.busy = False
        self.transport_object = None


class ParkingLot:

    def __init__(self):
        self.param = 'RandomSettings'
        self.rows = None
        self.columns = None
        self.size_list = None
        self.error_message = ''

    def get_config(self):
        if self.param is 'RandomSettings':
            rows_min, rows_max, cols_min, cols_max = config.Config().get_random_settings()
            self.rows = random.randint(rows_min, rows_max)
            self.columns = random.randint(cols_min, cols_max)
            self.size_list = [random.randint(1, 3) for row in range(self.rows)]
        if self.param is 'UserSettings':
            self.rows, self.columns, self.size_list = config.Config().get_user_settings()
            if self.rows != len(self.size_list):
                self.error_message = 'Wrong length parking lot size list!'
                logging.error(self.error_message)

    def create_parking_lot(self):
        self.get_config()
        if self.error_message != '':
            return [], self.error_message
        parking_lot = [[ParkingSpace() for column in range(self.columns)] for row in range(self.rows)]
        for row_index in range(len(self.size_list)):
            for place in parking_lot[row_index]:
                place.size = self.size_list[row_index]

        return parking_lot, self.error_message
