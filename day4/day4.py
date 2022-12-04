from day4_input import elf_pairs

# Part one
total_overlapping = 0
for pair in elf_pairs:
    if int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]):
        total_overlapping += 1
    elif int(pair[1][0]) >= int(pair[0][0]) and int(pair[1][1]) <= int(pair[0][1]):
        total_overlapping += 1

# Part two
range_overlapping = 0
for pair in elf_pairs:
    for i in range (int(pair[0][0]), int(pair[0][1])+1):
        if i in range(int(pair[1][0]), int(pair[1][1])+1):
            range_overlapping += 1
            break
        
print(range_overlapping)