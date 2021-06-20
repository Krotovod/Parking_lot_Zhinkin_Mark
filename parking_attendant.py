import logging

file_log = logging.FileHandler('Log.log')
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out),
                    format='[%(asctime)s | %(levelname)s]: %(message)s',
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)


class ParkingAttendant:

    def __init__(self):
        self.transport_number = 1
        self.parking_lot = None

    def park_transport(self, transport):
        logging.info(f'{transport.name} arrived at the parking lot.')
        for parking_row in self.parking_lot:
            if parking_row[0].size < transport.dimensions:
                continue
            for one_place in parking_row:
                if transport.size < 2 and one_place.is_busy is False:
                    one_place.is_busy = True
                    transport.number = self.transport_number
                    one_place.tech_value = transport
                    self.transport_number += 1
                    logging.info(f'{transport.name} parked.')
                    return
                if transport.size > 2 and one_place.is_busy is False:
                    first_free_place_index = parking_row.index(one_place)
                    last_free_place_index = first_free_place_index + transport.size
                    if len(parking_row[first_free_place_index:last_free_place_index]) != transport.size:
                        continue
                    if len(list(filter(lambda x: x.is_busy is False,
                                       parking_row[first_free_place_index:last_free_place_index]))) != transport.size:
                        continue
                    for pp in parking_row[first_free_place_index:last_free_place_index]:
                        pp.is_busy = True
                        transport.number = self.transport_number
                        pp.tech_value = transport
                    self.transport_number += 1
                    logging.info(f'{transport.name} parked.')
                    return

        logging.warning(f'For {transport.name} have no place.')

    def show_transports_list(self):
        list_of_transports = []
        for parking_row in self.parking_lot:
            find_transport_in_row = list(filter(lambda x: x.tech_value is not None, parking_row))
            list_of_transport_names = list(set([f'{x.tech_value.name}#{x.tech_value.number}' for x in
                                                find_transport_in_row]))
            list_of_transports += list_of_transport_names
        names_without_numbers = list(x.split('#')[0] for x in list_of_transports)
        transports_name_list = {i: names_without_numbers.count(i) for i in names_without_numbers}
        message = 'Transport parked: '
        for x in transports_name_list:
            message += f'"{x}" {transports_name_list[x]} pc., '
        logging.info(message[:-2])

    def show_parking_scheme(self):
        pl_columns = len(self.parking_lot[0])
        parking_scheme = '\n'
        for parking_row in self.parking_lot:
            list_parking_transports = list(x.tech_value.name[0] if x.tech_value is not None else ' ' for x in
                                           parking_row)
            parking_scheme += '--' * pl_columns + '-\n|' + '|'.join(list_parking_transports) + '|\n'
        parking_scheme += '--' * pl_columns + '-'
        logging.info(parking_scheme)

    def is_parking_full(self):
        count = 0
        for parking_row in self.parking_lot:
            count += len(list(filter(lambda x: x.is_busy is False, parking_row)))

        if count == 0:
            logging.warning(f'Parking lot is full!.')
