import re
# Global variables
input_path = 'input.txt'
input = []

# Read input file
with open(input_path, 'r') as file:
    for line in file:
        input.append(line.strip())

# Map words to words with the number inside -> The extra letters are for edge cases such as 'sevenine' -> this should
# return "79" and not "7ine".
number_mapping = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e',
}

total = 0
for line in input:
    for word, number in number_mapping.items(): #replace all words to "numbers" | For part 1 -> leave this out ;-)
        line = line.replace(word, number)

    numbers_str = re.findall(r'\d', line)  # Get each number individually to an array
    result_str = numbers_str[0] + numbers_str[-1]  # Join the first and last together
    total += int(result_str)  # Add that number to total

print(total)
