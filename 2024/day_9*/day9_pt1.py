# Open and read the contents of input_example.txt
with open('input.txt', 'r') as file:
    a = file.readline().strip()

# Convert the string of digits into a list of integers
a = [int(x) for x in a]

# Initialize the disk state
disk = []
block_id = 0
for i in range(len(a)):
    v = int(a[i])
    if i % 2 == 0:
        disk.extend([str(block_id)] * v)
        block_id += 1
    else:
        disk.extend(['.'] * v)

last = len(disk) - 1

# Iterate over the disk to compact it
for i in range(len(disk)):
    if disk[i] == '.':  # Find the first free space
        while last > i and disk[last] == '.':
            last -= 1  # Find the last occupied block
        if last <= i:
            break  # No more blocks to move
        # Move the block from last to i
        disk[i] = disk[last]
        disk[last] = '.'

# Calculate checksum based on the final state
checksum = 0
for i, block in enumerate(disk):
    if block != '.':
        checksum += i * int(block)

# Print only the checksum
print(checksum)