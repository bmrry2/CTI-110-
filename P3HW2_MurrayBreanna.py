# Breanna Murray
# October 2, 2026
# P3HW2
# This program will determine whether overtime was worked, calculate overtime pay, and calculate regular and gross pay for an employee based on their hours worked and hourly rate.


# Pseudocode

# Get Employee name, numbers of hours worked, employee pay rate 
name=input("Enter employee name:")
hours=float(input("Enter number of hours worked:"))
rate=float(input("Enter employee pay rate:"))

# Evaluate overtime
if hours > 40:
# Calculate reghour pay
    regular_pay=40*rate
# Calculate overtime pay
    overtime_hours=hours-40
    overtime_pay=overtime_hours*(rate*1.5)
# Calculate gross pay
    gross_pay=regular_pay+overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate


# Results
print()
print("----------------------------------------------------------------------------")
print("Employee Name: ", name)
print(f'{"Hours Worked":<15} {"Pay Rate":<12} {"Overtime Pay":<12} {"Regular Pay":<12} {"Gross Pay":<12}')
print("----------------------------------------------------------------------------")   
print(f'{hours:<15.1f}${rate:<12.2f}${overtime_pay:<12.2f}${regular_pay:<12.2f}${gross_pay:<12.2f}')