from day2_input import picks

# Part one
possible_outcomes = {
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}

total_score = 0
for pick in picks:
    print(pick)
    total_score += possible_outcomes[pick]

print(total_score)

# Part two
encrypted_elf_outcomes = {
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7
}

total_score_elf_stategy = 0
for pick in picks:
    print(pick)
    total_score_elf_stategy += encrypted_elf_outcomes[pick]
    
print(total_score_elf_stategy)