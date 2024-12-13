import os

# Define the file path for input_example.txt
file_path = 'input_example.txt'

# Define the possible directions for movement in the matrix (up, right, down, left)
alternatives = {
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
}

def dfs(mat, i, j, t, prev=-1):
    """
    Perform a depth-first search to find sequences incrementing by 1 from prev to target t.
    
    :param mat: The matrix to search.
    :param i: Current row index.
    :param j: Current column index.
    :param t: Target value to reach.
    :param prev: Previous value in the sequence.
    :return: A set of coordinates (i, j) that form a valid sequence.
    """
    # Print the current DFS call and its parameters
    print(f"DFS called at position ({i}, {j}) with prev={prev}")

    # Check boundary conditions
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[i]):
        return set()

    v = mat[i][j]  # Current matrix value

    # If the current value is not the next in sequence, return an empty set
    if v != prev + 1:
        return set()

    # If we've reached the target, return the current position
    if v == t:
        return {(i, j)}

    # Initialize a result set
    r = set()

    # Explore all possible directions
    for a in alternatives:
        ni, nj = i + a[0], j + a[1]  # Calculate the new indices
        r = r.union(dfs(mat, ni, nj, t, v))  # Recursive DFS call

    return r

# Read the matrix from the input file
with open(file_path, 'r') as file:
    mat = [[int(x) for x in line.strip()] for line in file]

# Print the input matrix for debugging
print("Input matrix:")
for row in mat:
    print(row)

s = 0  # Initialize the sum counter

# Iterate over each element in the matrix
for i in range(len(mat)):
    for j in range(len(mat[i])):
        # Check if the current element is the start of a sequence
        if mat[i][j] == 0:
            print(f"Starting DFS from position ({i}, {j})")
            r = dfs(mat, i, j, 9)  # Perform DFS to find sequences ending at 9
            print(f"Found sequence of length {len(r)} starting at ({i}, {j})")
            s += len(r)  # Add the length of the found sequence to the sum

# Print the final result
print("Total length of all sequences:", s)