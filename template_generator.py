import os
from datetime import datetime

# Get the current year
year = datetime.now().year

# Determine the base path where the script is located
base_script_path = os.path.dirname(os.path.abspath(__file__))

# Assume the AoC directory is the directory where the script is located
aoc_dir = base_script_path

# Define the base directory inside the 'AoC' folder using the current year
base_dir = os.path.join(aoc_dir, str(year))

# Check if there is a file or directory named after the current year
if os.path.exists(base_dir):
    if os.path.isdir(base_dir):
        print(f"The directory '{year}' already exists in 'AoC'. No folders or files were created.")
    else:
        print(f"A file named '{year}' already exists in 'AoC'. No folders or files were created.")
else:
    # Iterate through the day numbers from 1 to 25
    for day in range(1, 26):
        # Create the directory name for the current day
        day_dir = f'day_{day}'
        day_path = os.path.join(base_dir, day_dir)
        
        # Create the directory if it doesn't exist
        os.makedirs(day_path, exist_ok=True)
        
        # Define the filenames to be created within each day's directory
        filenames = [
            f'day{day}_pt1_example.py',
            f'day{day}_pt1.py',
            f'day{day}_pt2_example.py',
            f'day{day}_pt2.py',
            'input.txt',
            'input_example.txt'
        ]
        
        # Create each file within the current day's directory
        for filename in filenames:
            # Full path of the file to be created
            file_path = os.path.join(day_path, filename)
            
            # Create the file if it doesn't exist
            with open(file_path, 'w') as f:
                pass  # Creates an empty file

    print(f"Folders and files have been created successfully under 'AoC/{year}'.")