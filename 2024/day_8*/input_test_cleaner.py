# Open the input file for reading
with open("input_test.txt", "r") as file:
    # Read the content of the file
    data = file.readlines()

# Replace all occurrences of '#' with '.'
modified_data = [line.replace('#', '.') for line in data]

# Open the same file for writing to overwrite it
with open("input_test.txt", "w") as file:
    # Write the modified lines back to the file
    file.writelines(modified_data)

print("Replaced all '#' with '.' in the input file.")