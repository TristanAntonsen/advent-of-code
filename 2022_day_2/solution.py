with open('input.txt','r') as file:
    lines = file.read().strip()

games = lines.split("\n")

SCORES = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
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

total_score = 0
for game in games:
    move = game[-1]
    outcome = OUTCOMES[game]
    score = SCORES[outcome] + SCORES[move]
    total_score += score
    print(game, outcome, score, move) 
print(f"Total score: {total_score}")
