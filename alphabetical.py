file_path = "adjectives.txt"

# Read the lines from the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Sort the lines in alphabetical order
sorted_lines = sorted(lines)

# Write the sorted lines back to the file
with open(file_path, 'w') as file:
    file.writelines(sorted_lines)
