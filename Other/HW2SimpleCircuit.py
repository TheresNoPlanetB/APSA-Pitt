
print("Hello World!, This is SimpleCircuit.py , HW 3 in APSA. Starting...")

#DC Voltage Source, Called Vs with a value of 100V
#Connects to Bus 0
#Connects to Ristance Power lines with a resistance of 5 Ohms
#Connects to Bus 1
#Connects to RLoad 2000W at 100V nominal 
#Ends at a ground point

#calc volage at bus 0 in respect to refrence node Bus 0
#find line current
#easily modify the circuit by changing the values of the components
# Define the DC voltage source and its resistance

Vs =  100  # Voltage source in volts
R =  5     # Resistance in ohms

# Define the load
P =  2000  # Load power in watts
V =  100   # Nominal voltage in volts

# Calculate the current through the load
I_load = P / (V * V)  # Current in amperes (using P = IV)

# Calculate the voltage at bus  0 relative to reference node Bus  0
# Since Vs is connected to Bus  0 and Bus  1, the voltage at Bus  0 remains Vs
V_bus0 = Vs

# Calculate the line current
# Using Ohm's law I = V / R, where V is the voltage drop across the line
V_drop = V_bus0 - V  # Voltage drop across the line
I_line = V_drop / R  # Line current in amperes

# Output the calculated values
print(f"Voltage at bus  0 (relative to Bus  0): {V_bus0} V")
print(f"Line current: {I_line} A")

# Function to modify the circuit by changing the values of the components
def modify_circuit(new_Vs, new_R, new_P, new_V):
    global Vs, R, P, V
    Vs = new_Vs
    R = new_R
    P = new_P
    V = new_V
    I_load = P / (V * V)
    V_drop = V_bus0 - V
    I_line = V_drop / R
    print(f"\nModified Circuit Values:")
    print(f"New Voltage Source: {Vs} V")
    print(f"New Resistance: {R} Ohms")
    print(f"New Load Power: {P} W")
    print(f"New Nominal Voltage: {V} V")
    print(f"New Voltage at bus  0: {V_bus0} V")
    print(f"New Line Current: {I_line} A")

# Example usage of modify_circuit function
modify_circuit(120,  3,  1500,  90)
