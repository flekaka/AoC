from itertools import product

def calculate_total_calibration(file_path):
    # Initialize the total sum of test values that can be achieved
    total_sum = 0
    
    # Open the input file for reading
    with open(file_path, 'r') as file:
        # Process each line in the file
        for line in file:
            # Parse the line to get the test value and list of numbers
            test_value, numbers = parse_line(line)
            
            # Check if any combination of operators can produce the test value
            if can_produce_test_value(test_value, numbers):
                # If so, add the test value to the total sum
                total_sum += test_value
                
    # Return the total sum of all achievable test values
    return total_sum

def parse_line(line):
    # Split the line into test value and numbers using the colon as a separator
    parts = line.strip().split(':')
    # Convert the test value part to an integer
    test_value = int(parts[0].strip())
    # Convert the numbers part into a list of integers
    numbers = list(map(int, parts[1].strip().split()))
    return test_value, numbers

def can_produce_test_value(test_value, numbers):
    # Calculate the number of operators needed (one less than the number of numbers)
    num_operators = len(numbers) - 1
    # Generate all possible combinations of '+', '*', and '||' operators
    for operators in product(['+', '*', '||'], repeat=num_operators):
        # Evaluate the expression with the current combination of operators
        if evaluate_expression(numbers, operators) == test_value:
            # If the expression equals the test value, return True
            return True
    # Return False if no combination produces the test value
    return False

def evaluate_expression(numbers, operators):
    # Start with the first number as the initial result
    result = numbers[0]
    
    # Iterate over each operator and the corresponding number
    for i, operator in enumerate(operators):
        next_number = numbers[i + 1]
        # Apply the operator to the current result and the next number
        if operator == '+':
            result += next_number
        elif operator == '*':
            result *= next_number
        elif operator == '||':
            # Concatenate the numbers as strings and convert back to an integer
            result = int(str(result) + str(next_number))
    
    # Return the final calculated result
    return result

# Example usage:
file_path = 'input.txt'  # Replace with the path to your input file
total_calibration_result = calculate_total_calibration(file_path)
print(total_calibration_result)