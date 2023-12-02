import re
# Global variables
input_path = 'input.txt'
input = []

# Read input file
with open(input_path, 'r') as file:
    for line in file:
        input.append(line.strip())

# Part One
max_played_sets = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

total_possible_game_ids = 0
for game in input:
    valid_game = True
    colon_position = game.find(':') # Find the ":" position
    game_id = int(re.findall(r'\d+', game[:colon_position].strip())[0]) # Get the game ID from the string
    game_sets = re.split('; |, ', game[colon_position + 1:].strip()) # The remaining played sets
    for set in game_sets:
        color = re.sub(r'\d+', '', set).split()[0] # Get the color string from the input "green", "red" or "blue"
        amount = sum([int(num) for num in re.findall(r'\d+', set)]) # get the total amount for that color, in this set
        if max_played_sets[color] < amount: # Amount is higher than the allowed size, game is flagged as invalid
            valid_game = False
            break

    if valid_game:
        total_possible_game_ids += game_id # Adding the total up

print("Total possible game IDs: " + str(total_possible_game_ids))

# Part Two

total_power = 0
for game in input:
    possible_sets = dict.fromkeys(["green", "red", "blue"]) # Create empty dict for each game
    colon_position = game.find(':') # Find the ":" position
    game_id = int(re.findall(r'\d+', game[:colon_position].strip())[0]) # Get the game ID from the string
    game_sets = re.split('; |, ', game[colon_position + 1:].strip()) # The remaining played sets
    for set in game_sets:
        color = re.sub(r'\d+', '', set).split()[0] # Get the color string from the input "green", "red" or "blue"
        amount = sum([int(num) for num in re.findall(r'\d+', set)]) # get the total amount for that color, in this set
        if(possible_sets[color] == None or possible_sets[color] < amount): # If the amount is greater than the previous amount, add that amount to the set
            possible_sets[color] = amount

    power = 1
    for key, item in possible_sets.items(): # Multiply each minimum required cube
        power *= item

    total_power += power # Add it to the total

print("Total power: " + str(total_power))
