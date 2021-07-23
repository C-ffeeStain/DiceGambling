from random import randint,seed
import sys
from time import time
seed(time())

wins = 0
jackpots = 0
losses = 0

if len(sys.argv) >= 2: repeats = int(sys.argv[1])
else: repeats = 100


for x in range(repeats):
    number = randint(1, 6) + randint(1, 6)
    if number > 7:
        wins += 1
    if number == 7:
        jackpots += 1
    elif number < 7:
        losses += 1

print("Wins:", wins, "\nJackpots:", jackpots,"\nLosses:", losses)