def __init__
(self, buses, lines, transformers):
self.buses
= buses
self.lines = Lines
self-y_bus = None
1 usage
& Rafkorahim)
def y_bus_matrix(self):
# Initialize y_bus matrix with zeros
self.y_bus = pd.DataFrane(datanp.zeros( shape
[ten(self.buses), Len(self.buses)], typescomplex),
atypescomplex, index=[bus.none for bus in self.buses). columns=[bus.name for bus in self.buses])
# Populate y_bus natrix using prinitive admittance natrices fron Lines
for Line in self.Lines:
Y-prinitive • Line.prinitive_adeittance_natrix,line)
self update_y_bus(line.bus_a.nane, line.bus_b.nane, Y_prinitive)
# Populate y-bus natrix using prisitive admittance natrices fron transformers
for transformer in self.transformers:
Y_primitive = transformer.primitive_admittance_matrix_XFMRO
self.update_y_bus(transformer.bus_a.name, transforner.bus_b.name, Y_prinitive)
return self.y_bus
2 usages
4 Rafik Jibrahim
def update_y_bus(self, bus_a_name, bus_b_name, y_primitive):
self-y_bus.loc[bus_a_name,
bus_a_nane) += Y_primitive.loc(bus_a_name, bus_a_nane] * diagonal
self-y_bus.loc[bus_a_nane, bus_b_nane) += y_priaitive.loc[bus.aname, bus_b_nane] * of diagonal
self-y_bus.loc[bus_b_nane, bus_a_nane) + y_prinitive.loc[bus_b_name, bus_a_nane] * of diagonal self.y_bus.loc[bus_b_name,
bus_b_nane) += y_primitive.loc[bus_b_name, bus_b_name] = diagonal