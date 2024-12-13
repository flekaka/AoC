# Read input from the file and initialize the stones list
from collections import Counter

lines = open('input_example.txt', 'r').read().strip().split()
rocks = [int(a) for a in lines]

print("Initial stones:", rocks)

def Blink(rock:int):
    if rock == 0:
        return [1]
    elif len(str(rock)) % 2 == 0:
        strRock = str(rock)
        length = len(strRock)
        rock1 = int(strRock[:length // 2])
        rock2 = int(strRock[length // 2:])
        return [rock1, rock2]
    else:
        return [2024 * rock]

# Initialize a Counter to count occurrences of each rock
oldRocks = Counter(rocks)
print("Initial rock counts:", oldRocks)

# Simulate the process for 5 blinks
for b in range(0, 5):
    print(f"\nBlink {b+1}:")
    newrocks = {}
    for number, count in oldRocks.items():
        results = Blink(number)  # Transform the rock
        print(f"Rock {number} (count: {count}) transformed to {results}")
        for r in results:
            if r in newrocks:
                newrocks[r] += count
            else:
                newrocks[r] = count
    oldRocks = newrocks  # Update the Counter with new rock counts
    print("Rock counts after blink", b+1, ":", oldRocks)

# Calculate the total number of rocks after 5 blinks
answer2 = sum(oldRocks.values())
print(f"\nResult: {answer2}")