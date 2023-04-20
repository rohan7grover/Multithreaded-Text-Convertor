import os
import random
import string

# Set the directory path where you want to create the files
dir_path = "/Users/apple/Documents/TextChanger/input"

# Set the file size in characters (100MB)
file_size = 100000000

# Set the number of files to create
num_files = 20

# Define the character set to choose from
char_set = string.ascii_lowercase + string.digits

# Generate random data for each file
for i in range(num_files):
    # Create a new file with a unique name
    filename = f"file{i}.txt"
    filepath = os.path.join(dir_path, filename)
    with open(filepath, "w") as f:
        # Write random characters to the file
        random_chars = random.choices(char_set, k=file_size)
        f.write(''.join(random_chars))
