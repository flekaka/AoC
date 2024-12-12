from itertools import product

def calculate_total_calibration(file_path):
    total_sum = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            # Parse the line
            test_value, numbers = parse_line(line)
            print(f"Processing line: {line.strip()}")
            print(f"Test Value: {test_value}, Numbers: {numbers}")
            
            # Check if the test value can be produced
            if can_produce_test_value(test_value, numbers):
                print(f"Test value {test_value} can be achieved with numbers {numbers}. Adding to total sum.")
                total_sum += test_value
            else:
                print(f"Test value {test_value} cannot be achieved with numbers {numbers}.")
    
    print(f"Total calibration result: {total_sum}")
    return total_sum

def parse_line(line):
    parts = line.strip().split(':')
    print(f"Parts: {parts}")
    test_value = int(parts[0].strip())
    print(f"Test Value: {test_value}")
    numbers = list(map(int, parts[1].strip().split()))
    print(f"Numbers: {numbers}")
    return test_value, numbers

def can_produce_test_value(test_value, numbers):
    num_operators = len(numbers) - 1
    for operators in product(['+', '*'], repeat=num_operators):
        result = evaluate_expression(numbers, operators)
        print(f"Trying operators {operators} -> Result: {result}")
        if result == test_value:
            print(f"Success: {result} matches test value {test_value} with operators {operators}")
            return True
    return False

def evaluate_expression(numbers, operators):
    result = numbers[0]
    
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
    
    return result

# Example usage:
file_path = 'test_input.txt'  # Replace with the path to your input file
total_calibration_result = calculate_total_calibration(file_path)