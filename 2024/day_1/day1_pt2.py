# Initialize empty lists to hold the numbers from the input
list1 = []
list2 = []
similarity = 0  # Initialize the similarity score to 0

# Open the input file to read the data
with open("input.txt") as f:
    # Iterate over each line in the file
    for line in f:
        # Split the line into two values and convert them to integers
        num1, num2 = map(int, line.split())
        # Append the numbers to the respective lists
        list1.append(num1)
        list2.append(num2)

# Iterate through each number in list1
for num1 in list1:
    # Count how many times num1 appears in list2
    count = list2.count(num1)
    # Add to the similarity score (multiply num1 by the count)
    similarity += num1 * count

# Print the final similarity score
print("Similarity score:", similarity)
