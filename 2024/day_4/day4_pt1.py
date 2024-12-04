# Define directions for 8 possible moves: up, down, left, right, and 4 diagonals.
DIRECTIONS = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
    (-1, -1), # Diagonal up-left
    (-1, 1),  # Diagonal up-right
    (1, -1),  # Diagonal down-left
    (1, 1)    # Diagonal down-right
]

def read_input(file_path):
    """Reads the input file and returns a grid (list of lists)."""
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def check_word(grid, row, col, direction, word="XMAS"):
    """Checks if the word 'XMAS' exists starting from (row, col) in the given direction."""
    rows, cols = len(grid), len(grid[0])
    for i in range(len(word)):
        new_row = row + i * direction[0]
        new_col = col + i * direction[1]
        
        # Check if the new position is within bounds
        if not (0 <= new_row < rows and 0 <= new_col < cols):
            return False
        
        # Check if the character matches the expected letter in the word
        if grid[new_row][new_col] != word[i]:
            return False
    
    return True

def count_xmas(grid):
    """Counts all occurrences of the word 'XMAS' in the grid."""
    xmas_score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'X':  # Only start searching from 'X'
                for direction in DIRECTIONS:
                    if check_word(grid, row, col, direction):
                        xmas_score += 1
    return xmas_score

if __name__ == "__main__":
    # Read the grid from input.txt and count occurrences of "XMAS"
    grid = read_input("input.txt")
    result = count_xmas(grid)
    print(f"Total occurrences of 'XMAS': {result}")
