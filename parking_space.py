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
        self.is_busy = False
        self.tech_value = None


class ParkingLot:

    def __init__(self, param):
        self.param = param
        self.rows = None
        self.columns = None
        self.size_list = None
        self.error_message = ''

    def check_config(self):
        if self.param is 'random':
            pp_rows_min, pp_rows_max, pp_cols_min, pp_cols_max = config.Config().get_random_settings()
            self.rows = random.randint(pp_rows_min, pp_rows_max)
            self.columns = random.randint(pp_cols_min, pp_cols_max)
            self.size_list = [random.randint(1, 3) for rows in range(self.rows)]
        if self.param is 'user':
            self.rows, self.columns, self.size_list = config.Config().get_user_settings()
            if self.rows != len(self.size_list):
                logging.error('Wrong length parking lot size list!')
                self.error_message = 'Wrong length parking lot size list!'

    def create_parking_lot(self):
        self.check_config()
        if self.error_message != '':
            return [], self.error_message
        parking_lot = [[ParkingSpace() for pl_column in range(self.columns)] for pl_row in range(self.rows)]
        for row_index in range(len(self.size_list)):
            for place in parking_lot[row_index]:
                place.size = self.size_list[row_index]

        return parking_lot, self.error_message
