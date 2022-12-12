with open('input.txt','r') as file:
    lines = file.read().strip()

games = lines.split("\n")

SCORES = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'LOSS' : 0,
    'DRAW' : 3,
    'WIN' : 6
}
# A/X = Rock
# B/Y = Paper
# C/Z = Scissors

OUTCOMES = {
    'A X' : 'DRAW',
    'A Y' : 'WIN',
    'A Z' : 'LOSS',
    'B X' : 'LOSS',
    'B Y' : 'DRAW',
    'B Z' : 'WIN',
    'C X' : 'WIN',
    'C Y' : 'LOSS',
    'C Z' : 'DRAW'
}

OUTCOME_MOVES = {
    'DRAW' : {
        'A' : 'A',
        'B' : 'B',
        'C' : 'C'
    },
    'WIN' : {
        'A' : 'B',
        'B' : 'C',
        'C' : 'A'
    },
    'LOSS' : {
        'A' : 'C',
        'B' : 'A',
        'C' : 'B'
    }
}

NEW_CODES = {
    'X' : 'LOSS',
    'Y' : 'DRAW',
    'Z' : 'WIN'
}

# PART 1:
# total_score = 0
# for game in games:
#     move = game[-1]
#     outcome = OUTCOMES[game]
#     score = SCORES[outcome] + SCORES[move]
#     total_score += score
#     print(game, outcome, score, move) 
# print(f"Total score: {total_score}")

# PART 2:
total_score = 0
for game in games:
    outcome = NEW_CODES[game[-1]] # L/W/D based on key
    opponent_move = game[0] # A/B/C
    move = OUTCOME_MOVES[outcome][opponent_move] # A/B/C
    score = SCORES[outcome] + SCORES[move] # Score based on key
    total_score += score
    print(game, outcome, score, move) 
print(f"Total score: {total_score}")
