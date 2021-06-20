import configparser
import json


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.read("settings.ini")

    def get_random_settings(self):
        parking_lot_rows_min = json.loads(self.config.get("RandomSettings", "parking_lot_rows_min"))
        parking_lot_rows_max = json.loads(self.config.get("RandomSettings", "parking_lot_rows_max"))
        parking_lot_columns_min = json.loads(self.config.get("RandomSettings", "parking_lot_columns_min"))
        parking_lot_columns_max = json.loads(self.config.get("RandomSettings", "parking_lot_columns_max"))
        return parking_lot_rows_min, parking_lot_rows_max, parking_lot_columns_min, parking_lot_columns_max

    def get_user_settings(self):
        parking_lot_rows = json.loads(self.config.get("UserSettings", "parking_lot_rows"))
        parking_lot_columns = json.loads(self.config.get("UserSettings", "parking_lot_columns"))
        parking_lot_size_list = json.loads(self.config.get("UserSettings", "parking_lot_size_list"))
        return parking_lot_rows, parking_lot_columns, parking_lot_size_list
