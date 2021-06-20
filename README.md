# Parking_lot_Zhinkin_Mark
Test task for the position of a junior python developer.

## Structure and modules

#### Modules:
time, sys, logging, random, config

#### Structure:

`settings.ini` - config file. 

`parking_attendant.py` - module with the parking lot class.

`parking_space.py` - module with parking space and parking classes.

`transport.py` - module with a parent class transport. 

`main.py` - the initializing file.

## Description of the program logic

Initially, a parker attendant lot object and a parking space object are created. The parking space object is transferred
information what data to read from the config file - for parking by the user, or
generated randomly.

After reading the data from the config file, a two-dimensional array of the parking lot is created, which is output along with
a message about possible errors. If there is an error message, the program stops working.

After transferring the parking lot to the parker attendant, we begin to endlessly fill the parking lot with cars in a random sequence.

In the parking lot method _park_transport_, in turn, we check each row for compliance with the required dimension of parking spaces.
If, when checking the first place in a row, its size does not fit, move on to the next row.
In a row with a suitable dimension, we look through the places one by one. If the current place is taken, go to the next one.

If an empty space is found, a check is made for the size of the transport. For transport occupying one cell
 (cars and motorcycles) parking is easy. If the transport occupies more than 1 cell (bus), then the program looks for
 a place to fit transport.

If parking is successful or there is no necessary space for transport, a message is displayed.

In case of successful parking, the transport is assigned its serial number in the parking lot and the time of its removal.
After that, the vehicle object is transferred to the parking space object. This is necessary for
 displaying the number of vehicles in the parking lot.

After adding a transport, the parking attendant checks which transport needs to be removed in the _leaving_parking_lot_ method.

After removing the transport, the list of transport is displayed using the _parked_transport_ method and visualization
 using the _show_parking_scheme_ method.

Parking is checked for the absence of parking spaces using the _is_parking_full_ method, and if everything is busy, a message is displayed.

After 2 seconds, the cycle repeats.


## How to launch

1) Set the desired settings in the config file.
2) Change the _param_ property in the _ParkingLot_ class in the `main.py` file.
3) Run the file `main.py`.

