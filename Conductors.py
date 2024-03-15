
#This is where we will store the data of Conductor:


class ConductorData:

def init._(self, data):
    self.resistance_per_mile = data.get('resistance_per_mile', 0)
    self. reactance_per_mile = data-get('reactance_per_mile', 0)
    self. conductance_per_mile = data.get('conductance_per_mile', 0)
    self. susceptance_per_mile = data.get('susceptance_per_mile', 0)

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


