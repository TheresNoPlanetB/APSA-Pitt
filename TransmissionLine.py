# Here we form the Transmission line class (with child classes)

#Here we calculate series impedance,
# shunt admittance,
# primitive admittance matrix,
# and keeps track of connected buses •
# ##Should have child classes (e.g. conductor class)

class TransmissionLine:
    numbines = 5
_   registry - [)

def— init_(self, Busi, Bus2, condType, nunßundle, spacing, length, AB, BC, AC):
    self. registry-append(self)
    Line-numLines *= 1
    self.Busi = Busi
    self.Bus2 = Bus2
    self.condType = condType
    self.numßundle = numBundle self.spacing • spacing self. length - length self.Deg - getD_eq(AB, BC, AC)
    self.condinfo = getcondvalue(condtype)
    self.Reg = findResistanceE@(self.numBundle, self.condinfoe])
    self.R = findLineResistance(self.condInfo(1],self.numBundle,self.length)
    self. = findLineReactance(w,self.Deq, self.condInfo[2), self.length)
    self.B • findLineSusceptance(w,self.0eg, self.condInfo[2], self.length)

def calculate_series_impedance(self):
    # Implement the calculation of series impedance
    pass


def calculate_shunt_admittance(self):
    # Implement the calculation of shunt admittance
    pass


def calculate_primitive_admittance(self):
    # Implement the calculation of primitive admittance matrix
    pass