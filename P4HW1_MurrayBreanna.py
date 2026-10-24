# Breanna Murray
# 10/23/2026
# P4HW1
# Program will ask user to input the number of scores, evaluate if scores are valid between 0 and 100, and then program will display score list, lowest score, and caculated average


# Psuedocode
# Ask how many scores the user wants to enter
# Create an empty list to hold the scores
# Use a loop to enter the scores
# Check if the score is valid (between 0 and 100)
# If valid, add the score to the list
# If not valid, display an error message and ask for the score again
# After all scores are entered, display the list of scores
# Calculate the lowest score and display it
# Calculate the average score and display it


num_scores = int(input("How many scores do you want to enter? "))

scores = []

for item in range(num_scores):
    score=int(input("Enter score #" + str(item+ 1)+ " : "))

    while score < 0 or score > 100:
        print("INVALID score entered!!!!!")
        print("Score should be between 0 and 100.")
        score=int(input("Enter score #" + str(item+ 1)+ " again: "))
    scores.append(score)

lowest_score = min(scores)

print("Lowest score:", lowest_score)

modified_list = []
lowest_removed = False

for score in scores:
    if score == lowest_score and not lowest_removed:
        lowest_removed = True
        continue
    modified_list.append(score)

print("Scores without the lowest score:", modified_list)

total = 0


for score in modified_list:
    total = total + score

if len(modified_list) > 0:
    average_score = total / len(modified_list)
else:
    average_score = 0

print("Average score:", average_score)
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"


print("Scores entered:", scores)
print("Lowest score:", lowest_score)
print("Average score:", average_score)
print("Letter grade:", grade)    