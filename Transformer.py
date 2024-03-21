import numpy as np
import pandas as pd
from Bus import Bus
from Settings import Settings


#The Goal of This is to Calculate the
# transformer impedance,
# primitive admittance matrix


# Transformer 1
# 125 MVA
# Voltages; 20 kV∆/230 kV-Y,
# z = 0.085
# pu, x/r = 10


#Transformer 2
# 200 MVA
# Voltages; 20 kV∆/230 kV-Y,
# z = 0.105
# pu, x/r = 12


# Line Lengths
# L1: 10 miles
# L2: 25 miles
# L3 & L4: 20 miles
# L5: 10 miles
# L6: 35 miles


class Transformer:
    def __init__(self, name:str, bus1: Bus, bus2: Bus, power_rating, zpu: float, x_over_r_ratio: float):

        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.power_rating = power_rating
        self.x_over_r_ratio = x_over_r_ratio
        self.zpu = zpu  # Impedance per unit
        self.y_prim = pd.DataFrame(np.zeros((2,2),dtype= complex),dtype= complex, index=[self.bus1.name, self.bus2.name],columns=[self.bus1.name, self.bus2.name])
        # Initialize impedance and admittance matrices


    def calc_y_prim(self):
        # Assuming self.zpu is the positive sequence series impedance before any multiplication
        # Calculate positive sequence series impedance,

        self.zpu_complex = self.zpu * Settings.power_base / self.power_rating * np.exp(1j * np.arctan(self.x_over_r_ratio))
        # Calculate positive sequence shunt admittance
        ypu = 1 / self.zpu_complex
        # Construct the positive sequence shunt admittance matrix
        self.y_prim = np.array([[ypu, -ypu],  [-ypu, ypu]])


#testing
if __name__ == '__main__':
    bus_a = Bus("A",10)
    bus_b = Bus("B",10)
    # Example values for z and n (you need to replace these with actual values)
    tr1 = Transformer("tr1", bus_a, bus_b, 125, 0.085, 10)
    tr1.calc_y_prim()
    print(tr1.y_prim)

