# Initialize a counter to keep track of the number of safe reports.
safe_reports = 0

# Define a function that validates a list of numbers (report levels).
def validation(numbers):
    # Loop through each pair of adjacent numbers to check the difference.
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])  # Calculate the absolute difference between adjacent numbers.
        # If the difference is less than 1 or greater than 3, the report is unsafe.
        if diff < 1 or diff > 3:
            return False  # Exit early if the difference is invalid, report is unsafe.

    # Loop through each triplet of numbers to check if the trend (increasing or decreasing) is consistent.
    for j in range(len(numbers) - 2):
        # Ensure the levels are strictly increasing or decreasing (no switching).
        if numbers[j] > numbers[j + 1] < numbers[j + 2]:  
            return False  # If the trend switches from decreasing to increasing, it's unsafe.
        if numbers[j] < numbers[j + 1] > numbers[j + 2]:  
            return False  # If the trend switches from increasing to decreasing, it's unsafe.

    # If all checks pass, the report is considered safe.
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
        else: 
            # If the report is unsafe, check if removing one level makes it safe.
            for i in range(len(numbers)):  # Try removing each level one at a time.
                modified_report = []  # Create an empty list to store the modified report.
                
                # Loop through the original numbers, skipping the element at index i.
                for j in range(len(numbers)):
                    if j != i:
                        modified_report.append(numbers[j])  # Add the current number to the modified report.
                
                # Check if the modified report is now safe.
                if validation(modified_report):
                    safe_reports += 1  # Increment the counter if the modified report is safe.
                    break  # Stop checking once we find that removing one level makes it safe.

# Print the total number of safe reports.
print("Result:", safe_reports)
