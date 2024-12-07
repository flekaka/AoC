# Parse the input file into a grid representation using complex numbers
# Each position is represented as i + j*1j, where i is the row and j is the column
G = {i+j*1j: c for i, r in enumerate(open('input.txt'))
               for j, c in enumerate(r.strip())}

# Find the starting position of the guard, marked by '^'
start = min(p for p in G if G[p] == '^')

def walk(G):
    # Initialize position at the start, direction facing up (-1), and an empty set for seen positions
    pos, dir, seen = start, -1, set()
    # Continue moving while the position is within the map and the position-direction pair is new
    while pos in G and (pos, dir) not in seen:
        seen |= {(pos, dir)}  # Mark the current position and direction as seen
        if G.get(pos + dir) == "#":  # Check if there's an obstacle directly ahead
            dir *= -1j  # Turn right (90 degrees clockwise) if there's an obstacle
        else:
            pos += dir  # Move forward if the path is clear
    # Return the set of visited positions and whether a loop was detected
    return {p for p, _ in seen}, (pos, dir) in seen

# Calculate the path of distinct positions visited by the guard
path = walk(G)[0]

# Output the number of distinct positions visited and the count of positions 
# where adding an obstacle would cause the guard to get stuck in a loop
print(len(path),
      sum(walk(G | {o: '#'})[1] for o in path))