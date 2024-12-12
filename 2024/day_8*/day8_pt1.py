from collections import defaultdict

def inbounds(map, x, y):
    return 0 <= x < len(map[0]) and 0 <= y < len(map)

def antinodes_part1(p1, p2):
    p1_pts = set()

    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1

    if inbounds(data, x1 - dx, y1 - dy):
        p1_pts.add((x1 - dx, y1 - dy))

    if inbounds(data, x2 + dx, y2 + dy):
        p1_pts.add((x2 + dx, y2 + dy))

    return p1_pts

filename = "input.txt"

with open(filename) as file:
    data = file.read().strip().split("\n")

lut = defaultdict(list)
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == ".":
            continue
        lut[data[y][x]].append((x, y))

p1 = set()
for f, l in lut.items():
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            p1_pts = antinodes_part1(l[i], l[j])
            p1.update(p1_pts)

print(f"Part 1: {len(p1)}")