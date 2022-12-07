import os
from day7_input import input_cmd_seperated

# Part One
directories = {}
directories_sizes = {}
current_directory = ""
for line in input_cmd_seperated:
    if line[0] == '$':
        ds, cmd, *dir = line
        if cmd == 'cd':
            path = dir[0]
            if path == "/":
                current_directory = "/"
            else:
                current_directory = os.path.normpath(os.path.join(current_directory, path))
            
            if current_directory not in directories:
                directories[current_directory] = []
                directories_sizes[current_directory] = 0
    else:
        file_size, file_name = line
        if file_size != 'dir':
            directories_sizes[current_directory] += int(file_size)
        else:
            directories[current_directory].append(os.path.normpath(os.path.join(current_directory, file_name)))

def calculate_directory_size(dir):
    dirsize = directories_sizes[dir]
    for directory in directories[dir]:
        if directory in directories:
            dirsize += int(calculate_directory_size(directory))
    return dirsize

part_one_answer = 0
for directory in directories:
    dirsize = calculate_directory_size(directory)
    if dirsize <= 100000:
        part_one_answer += dirsize
        
print(part_one_answer)

# Part Two
total_space_available = 70000000
required_space = 30000000
space_already_used = calculate_directory_size("/")

directory_to_delete = total_space_available
for sizes in directories_sizes:
    dirsize = calculate_directory_size(sizes)
    if dirsize >= required_space - (total_space_available - space_already_used) and dirsize <= directory_to_delete:
        directory_to_delete = dirsize
        
print(directory_to_delete)