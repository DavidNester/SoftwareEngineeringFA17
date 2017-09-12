"""Module to simulate 100 games of a basketball drills"""

import random

#variable declaration (shPercent and numGames can be changed)
shPercent = .4
numGames = 100
made = 0
taken = 0
results = []

def shoot(m, t):
    """simulates shot taken returning 1 for make and 0 for miss"""
    rand = random.random()#generate random number from 0 to 1
    t += 1
    if rand < shPercent: #shot is made if r is less than shooting percentage
        m += 1
        return 1, m, t
    return 0, m, t

def playGame(m, t):
    """Simulates a full game returning 1 for win and 0 for loss"""
    recent = [-1]#list to remember most recent shots that are same
    while len(recent) < 3: #end loop if last 3 shots have bee the same
        sh, m, t = shoot(m, t) #get whether shot was made or missed
        if recent[-1] == sh:#compare to previous shot
            recent += [sh] #add if same
        else:
            recent = [sh] #create new list if different tha previous
    return recent[0], m, t #return win or loss

#repeat game numGames times
for i in range(numGames):
    result = playGame(made, taken) #add win (1) or loss (0) to results list
    results += [result[0]]
    made = result[1]
    taken = result[2]

print "This program simulates a basketball drill."
print "A player takes shots until they make 3 in a row (win) or miss three in a row (loss)."
print "The drill is simulated 100 times. "
print
#caclulate and print statistics
print "Games Played: " + str(numGames)
print "Shots Made: " + str(made)
print "Shots Taken: " + str(taken)
print "Shooting Percentage: " + str(round(made/float(taken), 2))
print "Wins: " + str(results.count(1))
print "Losses: " + str(results.count(0))
print "Winning Percentage: " + str(results.count(1) / float(numGames))
