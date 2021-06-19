class Transport:
    def __init__(self):
        self.dimensions = None
        self.name = None
        self.size = 1


class Motorcycle(Transport):
    def __init__(self):
        super().__init__()
        self.dimensions = 1
        self.name = 'Cycle'


class Car(Transport):
    def __init__(self):
        super().__init__()
        self.dimensions = 2
        self.name = 'Car'


class Bus(Transport):
    def __init__(self):
        super().__init__()
        self.dimensions = 3
        self.name = 'Bus'
        self.size = 5
