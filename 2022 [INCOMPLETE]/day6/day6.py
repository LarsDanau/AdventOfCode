from day6_input import characters

# Part One
def part_one():
    last_characters = characters[0:4]
    del characters[0:4]

    amount_processed = 4
    for i in range(len(characters)):
        dup = {x for x in last_characters if last_characters.count(x) > 1}
        if len(dup) == 0:
            break
        else:
            del last_characters[0]
            last_characters.append(characters[i])
        amount_processed += 1
        
    print(amount_processed)

# Part Two
def part_two():
    last_characters = characters[0:14]
    del characters[0:14]

    amount_processed = 14
    for i in range(len(characters)):
        dup = {x for x in last_characters if last_characters.count(x) > 1}
        if len(dup) == 0:
            break
        else:
            del last_characters[0]
            last_characters.append(characters[i])
        amount_processed += 1
        
    print(amount_processed)
    
# part_one()
# part_two()