# Initialize a counter to keep track of the number of safe reports.
safe_reports = 0

# Define a function that validates a list of numbers (report levels).
def validation(numbers):
    # Loop through each pair of adjacent numbers to check the difference.
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])  # Calculate the absolute difference.
        # If the difference is less than 1 or greater than 3, the report is unsafe.
        if diff < 1 or diff > 3:
            return False  # Exit early if the difference is invalid.

    # Loop through each triplet of numbers to check if the trend is consistent.
    for j in range(len(numbers) - 2):
        # Ensure the levels are strictly increasing or decreasing.
        if numbers[j] > numbers[j + 1] < numbers[j + 2]:  
            return False  # If it switches from decreasing to increasing, it's unsafe.
        if numbers[j] < numbers[j + 1] > numbers[j + 2]:  
            return False  # If it switches from increasing to decreasing, it's unsafe.

    # If all checks pass, the report is safe.
    return True

# Open the input file containing the reports.
with open('input.txt') as file:
    # Read each line (report) in the file.
    for line in file:
        # Convert the line of space-separated numbers into a list of integers.
        numbers = list(map(int, line.split()))
        # Validate the report; if it's safe, increment the counter.
        if validation(numbers):
            safe_reports += 1

# Print the total number of safe reports.
print("Result:", safe_reports)
