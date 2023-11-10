from day1_input import all_calories_input

calories_by_elf = all_calories_input.split('\n')

# Part one
max_calories = 0
current_elf_calories = 0
all_elf_calories = []
for calorie in calories_by_elf:
    if calorie == '':
        if current_elf_calories > max_calories:
            max_calories = current_elf_calories

        all_elf_calories.append(int(current_elf_calories))
        current_elf_calories = 0
    else:
        current_elf_calories += int(calorie)

# Part two
all_elf_calories.sort()
top_three_elfs = 0
for elf_calories in all_elf_calories[-3:]:
    top_three_elfs += elf_calories

print(top_three_elfs)
print(max_calories)