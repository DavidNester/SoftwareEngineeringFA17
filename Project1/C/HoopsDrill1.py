"""
Author: David Nester
Date: 9.21.2017
Module to simulate repeated basketball drills. Calculates statistics on wins and losses.
"""

from random import random
import time

# variable declaration (SHOOTING_PERCENT, NUM_GAMES, and SHOTS_NEEDED can be changed)
SHOOTING_PERCENT = .34
NUM_GAMES = 10000000
SHOTS_NEEDED = 5

WINS = 0

def shoot():
    """Simulates shot taken returning True for make and False for miss"""
    return random() <= SHOOTING_PERCENT

def play_game():
    """Simulates a full game returning True for win and False for loss"""
    made = 0
    missed = 0
    #can make this comparison because one of made or missed is always 0
    while made + missed < SHOTS_NEEDED:
        if shoot():
            made += 1
            missed = 0
        else:
            made = 0
            missed += 1
    return made > missed

if __name__ == "__main__":
    total = 0
    for j in range(10):
        START_TIME = time.time()
        for i in range(NUM_GAMES):
            if play_game():
                WINS += 1
        ELAPSED_TIME = time.time() - START_TIME
        print WINS
        total += WINS
        WINS = 0

    print "<=: " + str(total/10.0)
    """
    print "This program simulates a basketball drill."
    print "A player takes shots until they make " + str(SHOTS_NEEDED) + " in a row (win) or"
    print "miss " + str(SHOTS_NEEDED) + " in a row (loss)."
    print "The drill is simulated " + str(NUM_GAMES) + " times. \n"
    # caclulate and print statistics
    print "Games Played: " + str(NUM_GAMES)
    print "Shooting Percentage: " + str(SHOOTING_PERCENT)
    print "Shots Needed: " + str(SHOTS_NEEDED)
    print "Wins: " + str(WINS)
    print "Losses: " + str(NUM_GAMES-WINS)
    print "Winning Percentage: " + str(round(WINS / float(NUM_GAMES), 3))
    print "Elapsed Time: " + str(ELAPSED_TIME) + " seconds"
    """

"""
*******************************************************************************************
*************************************First Time Output*************************************
This program simulates a basketball drill.
A player takes shots until they make 5 in a row (win) or
miss 5 in a row (loss).
The drill is simulated 10000000 times.

Games Played: 10000000
Shooting Percentage: 0.34
Shots Needed: 5
Wins: 581455
Losses: 9418545
Winning Percentage: 0.058
Elapsed Time: 49.5608201027 seconds
*******************************************************************************************
*************************************Second Time Output************************************
This program simulates a basketball drill.
A player takes shots until they make 10 in a row (win) or
miss 10 in a row (loss).
The drill is simulated 10000000 times.

Games Played: 10000000
Shooting Percentage: 0.34
Shots Needed: 10
Wins: 25458
Losses: 9974542
Winning Percentage: 0.003
Elapsed Time: 448.240960836 seconds
"""
