import random

print "This program simulates a basketball drill where a player takes shots until they make 3 shots in a row (win) or miss three shots in a row (loss). The drill is simulated 100 times. "
print

def shoot():
    global made,taken #use global variables for total shots and made shots
    r = random.random()#generate random number from 0 to 1
    taken += 1
    if r < shPercent: #shot is made if r is less than shooting percentage
        made += 1
        return 1 #made
    return 0 #missed

def playGame():
    #plays full game and returns 1 for 1 and 0 for loss
    recent = [-1]#list to remember most recent shots that are same
    while len(recent) < 3: #end loop if last 3 shots have bee the same
        sh = shoot() #get whether shot was made or missed
        if recent[-1] == sh:#compare to previous shot
            recent += [sh] #add if same
        else:
            recent = [sh] #create new list if different tha previous
return recent[0] #return win or loss

#variable declaration (shPercent and numGames can be changed)
shPercent = .4
numGames = 100
made = 0
taken = 0
results = []

#repeat game numGames times
for i in range(numGames):
    #add win (1) or loss (0) to results list
    results += [playGame()]

#print and calculate statistics
winPercent = results.count(1) / float(numGames)
print "Games Played: " + str(numGames)
print "Shots Made: " + str(made)
print "Shots Taken: " + str(taken)
print "Shooting Percentage: " + str(made/float(taken))
print "Wins: " + str(results.count(1))
print "Losses: " + str(results.count(0))
print "Wining Percentage: " + str(winPercent)
