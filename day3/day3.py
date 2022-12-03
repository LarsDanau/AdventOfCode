from day3_input import rucksack_items_tuples, rucksack_items

print(rucksack_items_tuples)

# Part One
# Creating a priority table
priority_table = {}

priority_counter = 1
for x in range(ord('a'), ord('z')+1):
    priority_table[chr(x)] = priority_counter
    priority_counter += 1
    
for x in range(ord('A'), ord('Z')+1):
    priority_table[chr(x)] = priority_counter
    priority_counter += 1

print(priority_table)
total_priority = 0
for item_one, item_two in rucksack_items_tuples:
    for letter in item_one:
        if letter in item_two:
            total_priority += priority_table[letter]
            print(f"{letter} Found! Adding priority: {priority_table[letter]}. Total priority: {total_priority}")
            break

print(total_priority)

# Part Two
# Creating groups of three elfs
badge_groups = []
previous_index = 0
for i in range (3, len(rucksack_items)+1, 3):
    badge_groups.append(rucksack_items[previous_index: i])
    previous_index = i

total_group_priority = 0
for group in badge_groups:
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            total_group_priority += priority_table[letter]
            break
            
print(total_group_priority)