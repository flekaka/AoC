def read_input(file_path):
    """Reads the input file and returns a grid (list of lists)."""
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def count_x_mas_occurrences(grid):
    """
    Counts the occurrences of the "X-MAS" pattern in the grid.
    An "X-MAS" is defined as an 'A' with 'M' and 'S' in two opposite diagonal directions.
    """
    rows, cols = len(grid), len(grid[0])  # Dimensions of the grid.
    
    # Define the four diagonal directions as coordinate pairs (m, s).
    masks = [
        ((-1, -1), (1, 1)),  # Top-left to bottom-right diagonal.
        ((-1, 1), (1, -1)),  # Top-right to bottom-left diagonal.
        ((1, 1), (-1, -1)),  # Bottom-right to top-left diagonal (reverse).
        ((1, -1), (-1, 1))   # Bottom-left to top-right diagonal (reverse).
    ]
    total_count = 0  # Initialize the counter for "X-MAS" occurrences.

    # Iterate through each cell in the grid.
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'A':  # Check if the current cell contains 'A'.
                valid_diagonals = 0  # Tracks the number of valid diagonals for forming an "X-MAS".

                # Check each diagonal pattern defined in the masks.
                for mask in masks:
                    m_pos = (row + mask[0][0], col + mask[0][1])  # Position of 'M'.
                    s_pos = (row + mask[1][0], col + mask[1][1])  # Position of 'S'.

                    # Ensure both 'M' and 'S' positions are within bounds and match the expected letters.
                    if (
                        0 <= m_pos[0] < rows and 0 <= m_pos[1] < cols and
                        0 <= s_pos[0] < rows and 0 <= s_pos[1] < cols and
                        grid[m_pos[0]][m_pos[1]] == 'M' and
                        grid[s_pos[0]][s_pos[1]] == 'S'
                    ):
                        valid_diagonals += 1

                # If exactly two valid diagonals are found, an "X-MAS" is complete.
                if valid_diagonals == 2:
                    total_count += 1

    return total_count  # Return the total count of "X-MAS" occurrences.

if __name__ == "__main__":
    grid = read_input("input.txt")  # Read the input grid from the file.
    result = count_x_mas_occurrences(grid)  # Count the "X-MAS" occurrences.
    print(f"Total occurrences of 'X-MAS': {result}")  # Output the result.

