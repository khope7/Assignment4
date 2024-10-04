#Task 1: Given the two lists:

#submitted = ["Alice", "Bob", "Charlie", "David"]
#attended = ["Charlie", "Eve", "Alice", "Frank"]
#Find out if Alice submitted their assignment and attended class. HINT: How might the in keyword be of use here? And how can you check to see if Alice is in both submitted and attended in one if statement?


#Writing code to check for Alice in both lists and with else statement to catch for if not
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted their assignment and attended class.")
else:
    print("Alice has not both submitted their assignment and attended class.")