def guard_patrol(file_path):
    # Read the map input from the file
    with open(file_path, 'r') as file:
        map_lines = file.read().strip().split('\n')
    
    height = len(map_lines)
    width = len(map_lines[0])
    
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_index = 0  # Start facing up

    # Find the initial position and direction of the guard
    for r in range(height):
        for c in range(width):
            if map_lines[r][c] in '^v<>':
                pos = (r, c)
                if map_lines[r][c] == '^':
                    dir_index = 0
                elif map_lines[r][c] == '>':
                    dir_index = 1
                elif map_lines[r][c] == 'v':
                    dir_index = 2
                elif map_lines[r][c] == '<':
                    dir_index = 3
                break

    visited = set()
    visited.add(pos)

    while True:
        # Calculate the next position based on current direction
        next_pos = (pos[0] + directions[dir_index][0], pos[1] + directions[dir_index][1])

        # Check if the next position is out of bounds or an obstacle
        if (0 <= next_pos[0] < height and 0 <= next_pos[1] < width and 
            map_lines[next_pos[0]][next_pos[1]] != '#'):
            pos = next_pos  # Move forward
            visited.add(pos)
        else:
            # Turn right
            dir_index = (dir_index + 1) % 4

        # Check if the guard is out of bounds
        if not (0 <= pos[0] < height and 0 <= pos[1] < width):
            break

    return len(visited)

# Call the function with the path to the input file
result = guard_patrol('input.txt')
print(result)