import re

total_score = 0
filename = 'input.txt'

def extract_sections_from_file(filename):
    with open(filename, 'r') as file:
        input_string = file.read()
    
    # Regular expression pattern to match relevant instructions
    pattern = r"don't\(\)|do\(\)|mul\(\d+,\d+\)"
    
    # Find all occurrences of the pattern in the input string
    result = re.findall(pattern, input_string)
    
    return result

# Extract sections from the file
extracted_sections = extract_sections_from_file(filename)

# Initialize state variables
enabled = True  # Start with mul instructions enabled

# Now process each section
for section in extracted_sections:
    if section == "do()":
        enabled = True  # Enable future mul instructions
    elif section == "don't()":
        enabled = False  # Disable future mul instructions
    elif enabled and section.startswith("mul("):
        # Extract numbers from the 'mul' instruction
        numbers = re.findall(r'\d+', section)
        if len(numbers) == 2:
            x, y = map(int, numbers)
            total_score += x * y  # Add to total score

print("Total Score:", total_score)