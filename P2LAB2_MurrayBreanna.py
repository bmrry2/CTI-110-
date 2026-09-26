# Breanna Murray
# September 26, 2026
# Module 3 P2LAB2
# Program to calculate the amount of gas needed to travel a certain distance based on the miles per gallon of the vehicle.

# Pseudocode:
# 1. Create a dictionary containing the vehicle's make/model and their MPG
# 2. Get all the keys from the dictionary and store them 
# 3. Display the vehicle keys to the user
# 4. Ask the user to select a vehicle key
# 5. Display the MPG for the selected vehicle
# 6. Ask the user to input the miles they want to travel
# 7. Calculate the amount of gas needed to travel the distance based on the MPG

my_dict = {
    "Camaro": 18.21,
    "Prius": 52.36,  
    "Model S": 110,
    "Silverado": 26
}
keys = my_dict.keys()
print(keys) 

vehicle = input("Enter the vehicle: ")
print(f"{vehicle} gets {my_dict[vehicle]} MPG.")
miles = float(input("Enter the number of miles you want to travel: "))
gallons = miles / my_dict[vehicle]
print(f"Gallons of gas needed: {gallons:.2f}")
