import time
import itertools

# Define directions for 4 possible moves: up, down, left, right.
DIRECTIONS = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
]

def read_input(file_path): 
    """Reads the grid from the input file and returns it as a 2D list."""
    with open(file_path, 'r') as f:
        grid = [list(line.strip()) for line in f]
    return grid

def find_guard_start(grid):
    """Scans the grid to find the initial position of the guard (the '^' character).
    Returns the coordinates (row, column) of the guard's starting position."""
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '^':
                return (row, col)
    return None 

def is_within_bounds(position, grid):
    """
    Checks if the given position is within the boundaries of the grid.

    :param position: A tuple (row, col) representing the position to check.
    :param grid: A 2D list representing the grid.
    :return: True if the position is within bounds, False otherwise.
    """
    row, col = position
    rows, cols = len(grid), len(grid[0])
    
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

def is_obstacle(position, grid):
    """
    Checks if the given position contains an obstacle ('#').

    :param position: A tuple (row, col) representing the position to check.
    :param grid: A 2D list representing the grid.
    :return: True if it is an obstacle, False otherwise.
    """
    row, col = position
    return grid[row][col] == '#'

def move_guard(position, direction, directions):
    """
    Calculates the next position based on the current position and direction.

    :param position: A tuple (row, col) representing the current position of the guard.
    :param direction: An integer index representing the current direction the guard is facing.
    :param directions: A list of tuples representing the possible movement vectors.
    :return: A tuple (new_row, new_col) representing the new position after moving.
    """
    row, col = position
    d_row, d_col = directions[direction]  # Get the movement vector for the current direction
    return (row + d_row, col + d_col)  # Calculate and return the new position

def turn_right(direction_index):
    """
    Updates the direction index to turn right (90 degrees clockwise).

    :param direction_index: The current direction index.
    :return: The updated direction index after turning right.
    """
    return (direction_index + 1) % 4

def simulate_guard_path(grid):
    guard_position = find_guard_start(grid)
    direction_index = 0
    visited_positions = set()
    visited_positions.add(guard_position)

    spinner = itertools.cycle(['-', '\\', '|', '/'])  # Spinner characters

    while is_within_bounds(guard_position, grid):
        next_position = move_guard(guard_position, direction_index, DIRECTIONS)
        
        if not is_within_bounds(next_position, grid) or is_obstacle(next_position, grid):
            direction_index = turn_right(direction_index)
        else:
            guard_position = next_position
            visited_positions.add(guard_position)
        
        # Display spinner
        sys.stdout.write(next(spinner))  # Write next spinner character
        sys.stdout.flush()  # Flush to ensure character is printed
        sys.stdout.write('\b')  # Backspace to overwrite spinner character
        time.sleep(0.1)  # Pause for a short moment

    return len(visited_positions)

if __name__ == "__main__":
    # Read the grid from input.txt and count occurrences of "XMAS"
    grid = read_input("input.txt")
    result = simulate_guard_path(grid)
    print(f"Total visited positions: {result}")