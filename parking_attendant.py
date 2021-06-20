import logging

import random

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
        self.iteration = 0

    def park_transport(self, transport):
        logging.info(f'{transport.name} arrived at the parking lot.')
        self.iteration += 1
        transport.end_parking_time = self.iteration + random.randint(5, 10)
        for parking_row in self.parking_lot:
            if parking_row[0].size < transport.dimensions:
                continue
            for place in parking_row:
                if place.busy is True:
                    continue
                if transport.size == 1:
                    place.busy = True
                    transport.number = self.transport_number
                    place.transport_object = transport
                    self.transport_number += 1
                    logging.info(f'{transport.name} parked.')
                    return
                if transport.size > 1:
                    first_free_place_index = parking_row.index(place)
                    last_free_place_index = first_free_place_index + transport.size
                    transport_parking_area = parking_row[first_free_place_index:last_free_place_index]
                    if len(transport_parking_area) != transport.size:
                        continue
                    if len(list(filter(lambda x: x.busy is False, transport_parking_area))) != transport.size:
                        continue
                    for pp in transport_parking_area:
                        pp.busy = True
                        transport.number = self.transport_number
                        pp.transport_object = transport
                    self.transport_number += 1
                    logging.info(f'{transport.name} parked.')
                    return

        logging.warning(f'For {transport.name} have no place.')

    def leaving_parking_lot(self):
        for parking_row in self.parking_lot:
            list_leaving_transport = list(filter(lambda x: x.busy is True and x.transport_object.end_parking_time
                                                           == self.iteration, parking_row))

            leaving_transport_names = list(set([f'{x.transport_object.name}#{x.transport_object.number}' for x in
                                                list_leaving_transport]))
            for transport in leaving_transport_names:
                transport_type = transport.split("#")[0]
                logging.info(f'{transport_type} is leaving.')

            for pp in list_leaving_transport:
                pp.busy = False
                pp.transport_object = None

    def parked_transport(self):
        list_of_transports = []
        for parking_row in self.parking_lot:
            find_transport_in_row = list(filter(lambda x: x.transport_object is not None, parking_row))
            list_of_transport_names = list(set([f'{x.transport_object.name}#{x.transport_object.number}' for x in
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
            list_parking_transports = list(x.transport_object.name[0] if x.transport_object is not None else ' ' for x in
                                           parking_row)
            parking_scheme += '--' * pl_columns + '-\n|' + '|'.join(list_parking_transports) + '|\n'
        parking_scheme += '--' * pl_columns + '-'
        logging.info(parking_scheme)

    def is_parking_full(self):
        count = 0
        for parking_row in self.parking_lot:
            count += len(list(filter(lambda x: x.busy is False, parking_row)))

        if count == 0:
            logging.warning(f'Parking lot is full!.')
