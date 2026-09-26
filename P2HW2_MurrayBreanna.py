 # Breanna Murray
# September 26th, 2026
# P2HW2 - Grades List
# Collects six module grades, stores them in a list, and calculates the lowest, highest, and average grade.


# Psuedocode:
# 1. Ask for grades for six modules 
# 2. Store the grades in a list
# 3. Find the lowest grade in the list
# 4. Find the highest grade
# 5. Sum of all grades 
# 6. Calculate the average grade 
# 7. Print the lowest, highest, and average grades



module1= float(input("Enter grade for Module 1:"))
module2= float(input("Enter grade for Module 2:"))
module3= float(input("Enter grade for Module 3:"))
module4= float(input("Enter grade for module 4:"))
module5= float(input("Enter grade for Module 5:"))
module6= float(input("Enter grade for Module 6: "))

# Store all module grades in a list
grades = [module1, module2, module3, module4, module5, module6]

# Calculate the lowest, highest, and average grades
lowest_grade = min(grades)
highest_grade = max(grades)
total_sum = sum(grades)
average_grade = total_sum / len(grades)

# Print the results
print ()
print ("------------Results------------")
print(f"Lowest Grade:  {lowest_grade: .1f}")
print(f"Highest Grade: {highest_grade: .1f}")
print(f"Sum of Grades: {total_sum: .1f}")
print(f"Average:       {average_grade:.2f}") 
print ("--------------------------------")