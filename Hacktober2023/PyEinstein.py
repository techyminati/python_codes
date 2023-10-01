# Einsteins Famous Equation (E = mc ^2) or (E = mc squared)
# Ben Woodfield - proving the Power of Python
# 4 Lines of code, solve one of the greatest physics equations 

# Not sure if Energy Units are right


cSpeed = 299792458 # Metres Per Second Squared (m/s)2. Top 3 google results = this val
# m = 0.1 #Enter Value
mass = float(input("Enter Mass in Kg (eg: 10.99)\n>>> "))
energy = mass*cSpeed**2  #(m*c) * (m*c)
print("E = %d kg*(m/s)2" % energy) # Check Energy units





