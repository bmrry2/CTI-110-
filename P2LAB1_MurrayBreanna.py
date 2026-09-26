# Breanna Murray
# September, 26, 2026
# Module 3 P2LAB1
# Program to calculate circles diameter, circumference, and area. 

# Pseudocode: 
# 1. Math Module is imported 
# 2. Ask the user to input the radius of a circle
# 3. Convert the radius to a float
# 4. Calculate the diameter
# 5. Calculate the circumference
# 6. Calculate the area
# 7. Display the results to the user

import math

radius = float(input("Enter the radius of a circle: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2    


print ()
print (f"Radius: {radius}")
print (f"Diameter:{diameter: .2f}")
print (f"Circumference:{circumference: .2f}")
print (f"Area:{area: .2f}")