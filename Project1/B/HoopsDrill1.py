"""
Author: Brandon Chupp
Date: September 10, 2017

Programming Project One (Part A) - Basketball Practice Drill Simulation
"""
#DN -- Code works. There isnt really anything to change. Just small fixes to make shorter
#I interpreted the instructions as needing to report the shots made and taken during the simulation and
#then their shooting percentage from that but from reading it again I see that it can go both ways.
#It's definitely cleaner to do it this way (and nothing is gained from keeping track).
#Good Lint score
#Follows elements of good code (though they arent super applicable to a small program like this).

from random import random
import time

def made_shot(shooting_percentage):
    """
    Simulates a single shot. Returns true if the shot was made, otherwise false.
    shooting_percentage -- the player's percentage of makes
    """
    return random() <= shooting_percentage


def play_game():
    """
    Simulates playing a single game.
    Returns True if the game was won and False if it was lost.
    """
    made = 0
    missed = 0
    while missed < 5 and made < 5:
        if made_shot(.40):
            missed = 0
            made += 1
        else:
            made = 0
            missed += 1
    return made > missed

if __name__ == "__main__":
    won = 0
    lost = 0
    start_time = time.time()
    for i in range(10000000):
        if play_game():
            won += 1
        else:
            lost += 1
    elapsed_time = time.time() - start_time

    print "\nBasketball Practice Drill Simulation"
    print "--------------------------"
    print "This program simulates a basketball player shooting long-distance three-point shots and determines the " \
          "probability of the player winning the game.\n "
    print "Games played: 100"
    print "Consecutive shots needed to win: 3"
    print "Player's shooting percentage: 40%"
    print "Wins: " + str(won)
    print "Losses: " + str(lost)
    print "Winning percentage: " + str(won) + "%"
    print "Loss percentage: " + str(lost) + "%"
    print "Elapsed Time: " + str(elapsed_time)
