

#Here is Milestone 1

##calculate the positive sequence series impedance and shunt admittance matrices
###

#####
#given transformer system ratings and winding connection configurations
#given transmission line conductor data, line lengths, and tower drawings.
#This will be used to calculate the positive sequence series impedance and shunt admittance matrices.
#will use the data above and the one-line diagram to develop the positive sequence power flow system Ybus matrix.
#The computer program will be submitted along with a write up of the solution.
#Students are to type equations and results out rather than just copy and paste computer program outputs. Units should be included


#Text 3.1 - 3.5
#Text 4.2, 4.6, 4.20
#Class
#Raulo RadatzCoinstructor: Paulo Radatz Email: paulo.radatz@gmail.com Office Hours: By Appointment
#Teaching Assistant: Jack Carnovale, jac479@pitt.edu
#Prof Office 1238G Benedum Hall, Office Hours: Tuesdays, 11am-1pm
#Web


#DATA

#Transformer 1
#125 MVA
#Voltages; 20 kV∆/230 kV-Y,
#z = 0.085
#pu, x/r = 10


#Transformer 2?
#125 MVA
#Voltages; 20 kV∆/230 kV-Y,
#z = 0.085
#pu, x/r = 10

#Line Lengths

#L1: 10 miles
#L2: 25 miles
#L3 & L4: 20 miles
#L5: 10 miles
#L6: 35 miles

#ACSR is the line specifications
#0.647 dia inches
#0.0217 Feet
#460 amps
#



import numpy as np
import cmath as cmath

# Define the system parameters
transformers = {2}  # Transformer data
lines = {6}  # Transmission line data
nodes = {7}  # Node data

# Initialize the Ybus matrix
Ybus = np.zeros((len(nodes), len(nodes)), dtype=complex)

# Calculate the admittance for each transmission line and add it to the Ybus matrix
for line, data in lines.items():
    # Calculate the series impedance and shunt admittance
    z = complex(data['R'], data['X'])
    y_shunt = complex(0, data['B'])
    y_series = 1 / z

    # Get the from and to nodes for the line
    from_node = data['from']
    to_node = data['to']

    # Add the admittances to the Ybus matrix
    Ybus[from_node, from_node] += y_series + y_shunt / 2
    Ybus[to_node, to_node] += y_series + y_shunt / 2
    Ybus[from_node, to_node] -= y_series
    Ybus[to_node, from_node] -= y_series

# Add the transformer admittances to the Ybus matrix
for transformer, data in transformers.items():
    # Calculate the admittance
    z = complex(data['R'], data['X'])
    y = 1 / z

    # Get the from and to nodes for the transformer
    from_node = data['from']
    to_node = data['to']

    # Add the admittances to the Ybus matrix
    Ybus[from_node, from_node] += y
    Ybus[to_node, to_node] += y
    Ybus[from_node, to_node] -= y
    Ybus[to_node, from_node] -= y

print("Ybus matrix:")
print(Ybus)