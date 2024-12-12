from collections import defaultdict

def inbounds(map, x, y):
    return 0 <= x < len(map[0]) and 0 <= y < len(map)

def antinodes_part2(p1, p2):
    p2_pts = {p1, p2}
    
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1

    print(f"Processing antennas at {p1} and {p2}. dx={dx}, dy={dy}")

    # Extend before the first antenna
    curX, curY = x1, y1
    while True:
        curX -= dx
        curY -= dy
        if not inbounds(data, curX, curY):
            break
        print(f"Adding antinode before p1: {(curX, curY)}")
        p2_pts.add((curX, curY))

    # Extend after the first antenna
    curX, curY = x1, y1
    while True:
        curX += dx
        curY += dy
        if not inbounds(data, curX, curY):
            break
        print(f"Adding antinode after p1: {(curX, curY)}")
        p2_pts.add((curX, curY))

    return p2_pts

filename = "input_test.txt"

# Read and print the initial grid
with open(filename) as file:
    data = file.read().strip().split("\n")

print("Initial Grid:")
for line in data:
    print(line)
print("\n")

# Map frequencies to positions and print the mapping
lut = defaultdict(list)
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == ".":
            continue
        lut[data[y][x]].append((x, y))

print("Frequency to Positions Mapping:")
for frequency, positions in lut.items():
    print(f"Frequency '{frequency}': Positions {positions}")
print("\n")

p2 = set()
for f, l in lut.items():
    print(f"Processing frequency '{f}' with positions {l}")
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            p2_pts = antinodes_part2(l[i], l[j])
            p2.update(p2_pts)
    print(f"Accumulated antinodes: {p2}\n")

print(f"Part 2: {len(p2)}")