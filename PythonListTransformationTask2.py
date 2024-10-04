#Task 2: Calculate the average grade and print it.

#Copying list and code from PythonListTransformationTask1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()

grades.reverse()


#adding all numbers in list together used https://stackoverflow.com/questions/13909052/how-do-i-add-together-integers-in-a-list-sum-a-list-of-numbers-in-python for reference
total = sum(grades)

#created average and printed results
average = (total / len(grades))

print("Average of all grades:", average)