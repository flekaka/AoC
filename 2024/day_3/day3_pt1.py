import re

total_score = 0

filename = 'input.txt'

def extract_mul_sections_from_file(filename):
    # Read the content of the file
    with open(filename, 'r') as file:
        input_string = file.read()
    
    # Regular expression pattern to match 'mul(x,y)' where x and y are numbers
    pattern = r'mul\(\d+,\d+\)'
    
    # Find all occurrences of the pattern in the input string
    result = re.findall(pattern, input_string)
    
    return result

# Extract 'mul' sections
extracted_sections = extract_mul_sections_from_file(filename)

# Now extract numbers from the 'mul' sections
number_pattern = r'\d+'
number_result = []

# Extract numbers from each 'mul(x,y)' match
for section in extracted_sections:
    numbers = re.findall(number_pattern, section)
    number_result.extend(map(int, numbers))

# Multiply each even index element with the next odd index element and add to total_score
for i in range(0, len(number_result) - 1, 2):  # Step of 2 to get even and odd index pairs
    total_score += number_result[i] * number_result[i + 1]

print("Total Score:", total_score)