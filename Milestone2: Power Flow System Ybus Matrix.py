#  This is Milestone 2
#  Develop Power Flow System Ybus Matrix Checkoff

# Given transformer system ratings and winding connection configurations, transmission line conductor data, line, lengths, and tower drawings.
# This will be used to calculate the positive sequence series impedance and shunt admittance matrices.

# Use the data above and the one-line diagram to develop the positive sequence power flow system Ybus matrix.
# The computer program will be submitted along with a write up of the solution. Students are to type equations and results out rather than just copy and paste computer program outputs. Units should be


import numpy as np

# Assuming we have a list of transformers and transmission lines with their properties
# For simplicity, let's assume we have two transformers and two transmission lines

# Transformer 1
tr1 = {
    'name': 'Transformer 1',
    'bus1': 'Bus A',
    'bus2': 'Bus B',
    'zpu': 0.085, # Impedance per unit
    'x_over_r_ratio': 10, # Reactance over resistance ratio
    'power_rating': 125, # MVA
    'voltage1': 20, # kV
    'voltage2': 230 # kV
}

# Transformer 2
tr2 = {
    'name': 'Transformer 2',
    'bus1': 'Bus B',
    'bus2': 'Bus C',
    'zpu': 0.105,
    'x_over_r_ratio': 12,
    'power_rating': 200,
    'voltage1': 20,
    'voltage2': 230
}

# Transmission Line 1
tl1 = {
    'name': 'Transmission Line 1',
    'bus1': 'Bus A',
    'bus2': 'Bus B',
    'length': 10, # miles
    'conductor_data': {
        'resistance': 0.0001, # ohm/km
        'reactance': 0.0001, # ohm/km
        'shunt_admittance': 0.0001 # siemens/km
    }
}

# Transmission Line 2
tl2 = {
    'name': 'Transmission Line 2',
    'bus1': 'Bus B',
    'bus2': 'Bus C',
    'length': 25,
    'conductor_data': {
        'resistance': 0.0001,
        'reactance': 0.0001,
        'shunt_admittance': 0.0001
    }
}

# Placeholder function to calculate the Ybus matrix
def calculate_ybus(transformers, transmission_lines):
    # Initialize the Ybus matrix as a 3x3 matrix (for a 3-bus system)
    # In a real system, the size of the Ybus matrix would depend on the number of buses
    ybus = np.zeros((3, 3), dtype=complex)

    # Calculate the admittance of each transformer and transmission line
    # This is a simplified example. In a real scenario, you would need to consider the impedance and admittance matrices
    # of each transformer and transmission line, as well as the power flow conditions in the network.
    for tr in transformers:
        # Example calculation of transformer admittance
        # This should be replaced with the actual calculation based on the transformer's impedance and admittance matrices
        ybus[tr['bus1'], tr['bus1']] += 1 # Example: assuming a simple transformer with a single admittance value
        ybus[tr['bus2'], tr['bus2']] += 1

    for tl in transmission_lines:
        # Example calculation of transmission line admittance
        # This should be replaced with the actual calculation based on the transmission line's impedance and admittance matrices
        ybus[tl['bus1'], tl['bus1']] += 1 # Example: assuming a simple transmission line with a single admittance value
        ybus[tl['bus2'], tl['bus2']] += 1

    return ybus

# Example usage
transformers = [tr1, tr2]
transmission_lines = [tl1, tl2]
ybus = calculate_ybus(transformers, transmission_lines)
print(ybus)
