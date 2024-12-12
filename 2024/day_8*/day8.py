from collections import defaultdict
import sys

def inbounds(map, x, y):
    # Check if the coordinates (x, y) are within the bounds of the map
    return 0 <= x < len(map[0]) and 0 <= y < len(map)

def antinodes(p1, p2):
    # Calculate possible antinodes for two antennas (p1 and p2) of the same frequency
    p1_pts = set()  # Set to store antinodes where one antenna is twice as far from the midpoint
    p2_pts = {p1, p2}  # Set to store all possible positions for part two

    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1  # Horizontal distance between p1 and p2
    dy = y2 - y1  # Vertical distance between p1 and p2

    # Calculate antinode before the first antenna (p1)
    if inbounds(data, x1 - dx, y1 - dy):
        p1_pts.add((x1 - dx, y1 - dy))

    # Calculate antinode after the second antenna (p2)
    if inbounds(data, x2 + dx, y2 + dy):
        p1_pts.add((x2 + dx, y2 + dy))

    # For Part 2: add all positions between and extending beyond p1 and p2
    curX, curY = x1, y1
    while True:
        curX -= dx
        curY -= dy
        if not inbounds(data, curX, curY):
            break
        p2_pts.add((curX, curY))

    curX, curY = x1, y1
    while True:
        curX += dx
        curY += dy
        if not inbounds(data, curX, curY):
            break
        p2_pts.add((curX, curY))

    return p1_pts, p2_pts

# Set the default file name to read the map of antennas
filename = "input.txt"

# Read the file content into a list of strings (each representing a row of the map)
try:
    with open(filename) as file:
        data = file.read().strip().split("\n")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    sys.exit(1)

# Create a dictionary mapping each frequency to a list of its antenna positions
lut = defaultdict(list)
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == ".":
            continue
        lut[data[y][x]].append((x, y))

p1 = set()  # Set to store unique antinodes for Part 1
p2 = set()  # Set to store unique antinodes for Part 2
for f, l in lut.items():
    # For each frequency, compare all pairs of antennas
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            p1_pts, p2_pts = antinodes(l[i], l[j])
            p1.update(p1_pts)  # Update Part 1 antinodes
            p2.update(p2_pts)  # Update Part 2 antinodes

# Output the number of unique antinodes for Part 1 and Part 2
print(f"Part 1: {len(p1)}")
print(f"Part 2: {len(p2)}")