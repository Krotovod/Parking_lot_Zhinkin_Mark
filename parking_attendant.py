import logging

file_log = logging.FileHandler('Log.log')
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out),
                    format='[%(asctime)s | %(levelname)s]: %(message)s',
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)


class ParkingAttendant:

    def park_transport(self, parking_place, transport):
        for parking_row in parking_place:
            if parking_row[0].size < transport.dimensions:
                continue
            for one_place in parking_row:
                if transport.size < 2 and one_place.is_busy is False:
                    one_place.is_busy = True
                    logging.info(f'{transport.name} припаркован успешно.')
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
                    logging.info(f'{transport.name} припаркован успешно.')
                    return

        logging.info(f'Транспортное средство {transport.name} не припарковано!.')
