# Initialize empty lists to hold the numbers from the input
list1 = []
list2 = []
differences = []

# Open the input file to read the data
with open("input.txt") as f:
    # Iterate over each line in the file
    for line in f:
        # Split the line into two values and convert them to integers
        num1, num2 = map(int, line.split())
        # Append the numbers to the respective lists
        list1.append(num1)
        list2.append(num2)
        
        # Sort both lists after each new line is added (could be moved outside the loop for efficiency)
        list1.sort()
        list2.sort()

    # Calculate the absolute differences between corresponding elements in the two sorted lists
    for num1, num2 in zip(list1, list2):
        differences.append(abs(num2 - num1))  # Take the absolute value to ensure positive differences

# Sum all the absolute differences
total_difference = sum(differences)

# Print the total result (sum of the absolute differences)
print("Result:", total_difference)
