def remove_duplicates(file_path):
    lines = set()
    with open(file_path, 'r') as file:
        for line in file:
            lines.add(line.strip())
    
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(line + '\n')

# Usage example
file_path = 'nouns.txt'
remove_duplicates(file_path)
