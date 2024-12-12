# Open and read the contents of input_example.txt
with open('input_example.txt', 'r') as file:
    a = file.readline().strip()

# Convert the string of digits into a list of integers
a = [int(x) for x in a]

# Function to print the current state of the disk based on the internal representation
def print_disk_state(a):
    disk = []
    block_id = 0
    for i in range(len(a)):
        v = int(a[i])
        if i % 2 == 0:
            disk.extend([str(block_id)] * v)
            block_id += 1
        else:
            disk.extend(['.'] * v)
    print(''.join(disk))

print("Initial state:")
print_disk_state(a)

sum = 0
block = 0
last = len(a) - 1

# Iterate over the list a
for i in range(len(a)):
    v = int(a[i])
    if i % 2 == 0:
        for _ in range(v):
            sum += ((i // 2) * block)
            block += 1
    elif last > i:
        for _ in range(v):
            while last > i and a[last] == 0:
                last -= 2
            if last <= i:
                break
            sum += ((last // 2) * block)
            block += 1
            a[last] -= 1
            a[i] += 1  # Move the block to the current free space
            print(f"After moving block at position {last}:")
            print_disk_state(a)

print("Final state:")
print_disk_state(a)
print("Checksum:", sum)