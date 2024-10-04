#Task 2: Extract all the temperatures above 100. HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.


#Copying code from AdvSlicingTechniquesTask1 used https://stackoverflow.com/questions/11978088/python-list-comprehension-learnpython-org for reference, did not include 100 as is not over 100
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

#Copys value to hightemp list only if the value is over 100 and prints total hightemp list
hightemp = [x for x in temperatures if x > 100]

print(hightemp)