# Read input from the file and initialize the stones list
lines = open('input_example.txt', 'r').read().strip().split()
rocks = [int(a) for a in lines]

print("Initial stones:", rocks)

def Blink(rock: int):
    """
    Determine the transformation of a rock based on its current number.
    
    :param rock: The current number on the rock.
    :return: A list of new rocks after applying the transformation rules.
    """
    if rock == 0:
        print(f"Rock {rock} transformed to [1]")
        return [1]
    elif len(str(rock)) % 2 == 0:
        strRock = str(rock)
        length = len(strRock)
        rock1 = int(strRock[:length // 2])
        rock2 = int(strRock[length // 2:])
        print(f"Rock {rock} transformed to [{rock1}, {rock2}]")
        return [rock1, rock2]
    else:
        new_rock = 2024 * rock
        print(f"Rock {rock} transformed to [{new_rock}]")
        return [new_rock]

# Simulate the process for 5 blinks
for i in range(5):
    print(f"\nBlink {i+1}:")
    newRocks = []
    for rock in rocks:
        newRocks.extend(Blink(rock))  # Apply Blink transformation to each rock
    rocks = newRocks  # Update the rocks list with the new arrangement
    print("Stones after blink", i+1, ":", rocks)

# Calculate and print the result after 5 blinks
answer1 = len(rocks)
print(f"\npart 1: {answer1}")