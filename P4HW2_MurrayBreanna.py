# Breanna Murray
# 10/24/2026
# P4HW2
# Calculate gross pay for multiple employees and total amount paid for regular pay and total amount paid for all employees


# Psuedocode
# Ask user for employee name, hours worked, and hourly pay rate
# Create accumulator variables for total regular pay and total gross pay
# Add Employee count plus one
# Evaluate overtime pay if hours worked is greater than 40
# Ask User employee info
# Calculate employee pay
# Add to accumulator totals
# Display results for the employee


name = input("Enter employee name or 'done' to finish: ")

overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'done':
    employee_count += 1 

    hours = float(input("How many hours did "  + name + " work this week? "))
    rate = float(input("What is " + name + " hourly pay rate? "))

    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        regular_pay = 40 * rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_pay = 0
        overtime_hours = 0
        regular_pay = hours * rate
        gross_pay = regular_pay

    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay


    print(f"-------------------------------")
    print("employee Name:",name)
    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}')
    print("-----------------------------------------------------------------------")
    print(f'{hours:<15}{rate:<12}{overtime_pay:<15}{regular_pay:<15}{gross_pay:<12}')


    name = input("Enter employee name or 'done' to finish: ")

print("Total number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${overtimepay_total:.2f}")
print(f"Total amount paid for regular time: ${regularpay_total:,.2f}")
print(f"Total amount paid in gross: ${grosspay_total:,.2f}")