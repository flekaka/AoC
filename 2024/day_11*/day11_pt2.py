# Read input from the file and initialize the stones list
from collections import Counter

lines = open('input.txt', 'r').read().strip().split()
rocks = [int(a) for a in lines]

def Blink(rock:int):
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if rock == 0:
        return [1]
    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
    # The left half of the digits are engraved on the new left stone, 
    # and the right half of the digits are engraved on the new right stone. 
    elif len(str(rock)) %2 == 0:
        strRock = str(rock)
        length = len(strRock)
        rock1 = int(strRock[:length//2])
        rock2 = int(strRock[length//2:])
        return [rock1, rock2]
    # If none of the other rules apply, the stone is replaced by a new stone; 
    # the old stone's number multiplied by 2024 is engraved on the new stone.
    else:
        return [2024 * rock]

# Initialize a Counter to count occurrences of each rock
oldRocks = Counter(rocks)

# Simulate the process for 75 blinks
for b in range(0, 75):
    newrocks = {}
    # Iterate over each unique rock and its count
    for number, count in oldRocks.items():
        results = Blink(number)  # Transform the rock
        # Update the newrocks dictionary with transformed results
        for r in results:
            if r in newrocks:
                newrocks[r] += 1 * count
            else:
                newrocks[r] = 1 * count
    oldRocks = newrocks  # Update the Counter with new rock counts

# Calculate the total number of rocks after 75 blinks
answer2 = 0
for number, count in oldRocks.items():
    answer2 += count

print(f'Result: {answer2}')