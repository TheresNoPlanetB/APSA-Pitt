#This keeps track of bus name, index, and nominal voltage

class Bus:

    counter = 0

    def __init__(self, name, index, base_kv, nominal_voltage):
        self.name = name
        self.index = Bus.counter
        self.base_kv = base_kv
        self.index = index
        self.v = None
        self.nominal_voltage = nominal_voltage

        Bus.counter = Bus.counter + 1

