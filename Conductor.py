
#This is where we will store the data of Conductor:


class Conductor:


# ACSR is the line specifications
# 0.647 dia inches
# 0.0217 Feet
# 460 amps


reactance =

# Line Lengths (miles)
L1 = 10
L2 =25
L3 = 20
L4 = 20
L5 = 10
L6 = 35

WHAT DATA


self.bus_order: List[str] = list()
self.buses: Dict[str, Transformer] = dict()
self.transformers; Dict[str, Transformer ] = dict()

def init._(self, data):
    self.resistance_per_mile = data.get('resistance_per_mile', 0)
    self.reactance_per_mile = data-get('reactance_per_mile', 0)
    self.conductance_per_mile = data.get('conductance_per_mile', 0)
    self.susceptance_per_mile = data.get('susceptance_per_mile', 0)




def calculate_impedance(self):
    # Here we Calculate impedance based on conductor data and line length
    #   impedance = R + j*X, where R is resistance and X is reactance
    resistance = self.conductor_data['resistance_per_unit_length'] * self.length
    reactance = self.conductor _data['reactance_per_unit_length'] * self.length
    impedance = resistance + 1j * reactance
    return impedance

def calculate_admittance(self):
    # Implement calculation of shunt admittance
    # Example calculation using simple formula:
    # admittance = 6 + j*B, where 6 is conductance and B is susceptance
    conductance = self.conductor_data['conductance_per_unit_length'] * self.length
    susceptance = self.conductor_datal 'susceptance_per_unit_length') * self. length
    admittance = conductance + 1j * susceptance
    return admittance


