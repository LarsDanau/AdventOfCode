from day5_input import input_moves

stacks = [["T", "D", "W", "Z", "V", "P"], ["L", "S", "W", "V", "F", "J", "D"], ["Z", "M", "L","S","V","T", "B", "H"],
          ["R", "S", "J"], ["C", "Z", "B", "G", "F", "M", "L", "W"], ["Q", "W", "V", "H", "Z", "R", "G", "B"], ["V", "J", "P", "C", "B", "D", "N"], ["P", "T", "B", "Q"], ["H", "G", "Z", "R", "C"]]

# Part One
moves = []
for move in input_moves.split('\n'):
    cmds = move.split()
    amount = int(cmds[1])
    from_stack = int(cmds[3]) - 1
    to_stack = int(cmds[5]) - 1
    for i in range(1, amount +1):
        try:
            stacks[to_stack].append(stacks[from_stack].pop())
        except IndexError:
            break
        
combined_letters = ""
for stack in stacks:
    combined_letters += stack[-1]

stacks = [["T", "D", "W", "Z", "V", "P"], ["L", "S", "W", "V", "F", "J", "D"], ["Z", "M", "L","S","V","T", "B", "H"],
          ["R", "S", "J"], ["C", "Z", "B", "G", "F", "M", "L", "W"], ["Q", "W", "V", "H", "Z", "R", "G", "B"], ["V", "J", "P", "C", "B", "D", "N"], ["P", "T", "B", "Q"], ["H", "G", "Z", "R", "C"]]

# Part Two
for move in input_moves.split('\n'):
    cmds = move.split()
    amount = int(cmds[1])
    from_stack = int(cmds[3]) - 1
    to_stack = int(cmds[5]) - 1
    crate_order = []
    for i in range(0, amount):
        letter = stacks[from_stack].pop()
        crate_order.insert(0, letter)
    for letter in crate_order:
        stacks[to_stack].append(letter)
        
combined_letters = ""
for stack in stacks:
    combined_letters += stack[-1]
    
print(combined_letters)