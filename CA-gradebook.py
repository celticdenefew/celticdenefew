last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:
## List of classes
subjects = ["physics", "calculus", "poetry", "history"]
## List of grades
grades = [98, 97, 85, 88]

## Combine the two manually
gradebook = [["physics", 98], ["calclus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)
print()

## Add class and grade x2
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)
print()

## Adjust a grade with math
gradebook[5][1] = gradebook[5][-1] + 5
print(gradebook)
print()

## Adjusting Poetry to Pass/Fail
# gradebook[2].remove(85)
# print(gradebook)
# print()

if gradebook[2][1] >= 70:
    gradebook[2][1] = "Pass"
print(gradebook)
print()
