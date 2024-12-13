import os

# Define the possible directions for movement in the matrix (up, right, down, left)
alternatives = {
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
}

def dfs(mat, i, j, t, prev=-1):
    """
    Perform a depth-first search to find hiking trails starting at height 0 and ending at height 9.
    
    :param mat: The matrix to search.
    :param i: Current row index.
    :param j: Current column index.
    :param t: Target height to reach (9).
    :param prev: Previous height in the sequence (default is -1).
    :return: The number of distinct trails reaching the target.
    """
    # Check boundary conditions
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[i]):
        return 0

    v = mat[i][j]  # Current matrix value

    # If the current value is not the next in sequence, return 0
    if v != prev + 1:
        return 0

    # If we've reached the target height, count this as a valid trail
    if v == t:
        return 1

    # Initialize a result counter for distinct trails
    r = 0

    # Explore all possible directions
    for a in alternatives:
        ni, nj = i + a[0], j + a[1]  # Calculate the new indices
        r += dfs(mat, ni, nj, t, v)  # Recursive DFS call

    return r

# Read the matrix from the input file
file_path = 'input_example.txt'
with open(file_path, 'r') as file:
    mat = [[int(x) for x in line.strip()] for line in file]

# Print the input matrix for debugging
print("Input matrix:")
for row in mat:
    print(' '.join(map(str, row)))

s = 0  # Initialize the sum of trailhead ratings

# Iterate over each element in the matrix
for i in range(len(mat)):
    for j in range(len(mat[i])):
        # Check if the current element is a trailhead (height 0)
        if mat[i][j] == 0:
            print(f"Processing trailhead at position ({i}, {j})")
            r = dfs(mat, i, j, 9)  # Perform DFS to find trails ending at height 9
            print(f"Trailhead at ({i}, {j}) has a rating of {r}")
            s += r  # Add the trailhead's rating to the total sum

# Print the final result
print("Total sum of all trailhead ratings:", s)