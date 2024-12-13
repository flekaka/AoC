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
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if rock == 0:
        print(f"Rock {rock} transformed to [1]")
        return [1]
    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
    # The left half of the digits are engraved on the new left stone,
    # and the right half of the digits are engraved on the new right stone.
    elif len(str(rock)) % 2 == 0:
        strRock = str(rock)
        length = len(strRock)
        rock1 = int(strRock[:length // 2])
        rock2 = int(strRock[length // 2:])
        print(f"Rock {rock} transformed to [{rock1}, {rock2}]")
        return [rock1, rock2]
    # If none of the other rules apply, the stone is replaced by a new stone;
    # the old stone's number multiplied by 2024 is engraved on the new stone.
    else:
        new_rock = 2024 * rock
        print(f"Rock {rock} transformed to [{new_rock}]")
        return [new_rock]

# Simulate the process for 6 blinks
for i in range(6):
    print(f"\nBlink {i+1}:")
    newRocks = []
    for rock in rocks:
        newRocks.extend(Blink(rock))  # Apply Blink transformation to each rock
    rocks = newRocks  # Update the rocks list with the new arrangement
    print("Stones after blink", i+1, ":", rocks)

# Calculate and print the result after 6 blinks
answer1 = len(rocks)
print(f"\npart 1: {answer1}")