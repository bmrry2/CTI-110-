# Breanna Murray    
# September 30th, 2026
# P3HW1
# This program takes a number grade, determines lowest, highest, sum and average for grades and displays letter grade.


# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

print()
print("-------------Results-------------")
low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)

print()
print("Lowest grade: ", low)
print("Highest grade: ", high) 
print("Sum of grades: ", sum)
print("Average: ", format(avg, ".2f"))   
print()
print("-----------------------------------")


# Determine letter grade for average

if avg >= 90:
    print("Your grade is: A")
elif avg >= 80:
    print("Your grade is: B")
elif avg >= 70:
    print("Your grade is: C")
elif avg >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F") 