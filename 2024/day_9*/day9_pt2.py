# Open and read the contents of input.txt
with open('input.txt', 'r') as file:
    a = file.readline().strip()

# Convert the string of digits into a list of integers
a = [int(x) for x in a]

# Initialize the disk state
disk = []
file_lengths = []
block_id = 0
for i in range(len(a)):
    v = int(a[i])
    if i % 2 == 0:
        disk.extend([str(block_id)] * v)
        file_lengths.append((block_id, v))  # Store file ID and its length
        block_id += 1
    else:
        disk.extend(['.'] * v)

# Reverse the file list to process files in decreasing order of file ID
file_lengths.sort(reverse=True, key=lambda x: x[0])

for file_id, length in file_lengths:
    # Find the start position of the file
    start_pos = disk.index(str(file_id))
    
    # Find the leftmost suitable free space span
    free_span_start = None
    free_span_length = 0
    
    i = 0
    while i < start_pos:
        if disk[i] == '.':
            if free_span_start is None:
                free_span_start = i
            free_span_length += 1
        else:
            free_span_start = None
            free_span_length = 0
        
        # Check if the current span is suitable
        if free_span_length >= length:
            # Move the file to the free space
            disk[free_span_start:free_span_start + length] = [str(file_id)] * length
            disk[start_pos:start_pos + length] = ['.'] * length
            break
        
        i += 1

# Calculate checksum based on the final state
checksum = 0
for i, block in enumerate(disk):
    if block != '.':
        checksum += i * int(block)

# Print only the checksum
print(checksum)