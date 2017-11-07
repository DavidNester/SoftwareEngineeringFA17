from calculations import *

print 'This program is a simulation of the route a robot can take to pick up boxes.'
print 'The robot can pick up two boxes at once.\n'

package_locations = [[1.0,1.0],[2,2]]

DISTANCE_TO_HOME = 300

order = []

total_dist = 0

while len(package_locations) > 1:

    total_dist += DISTANCE_TO_HOME #Drive from home to corner

    package = package_locations[0] #Get the first package

    package_locations.pop(0) #Deletes first package

    order.append(package) #Adds it to the order

    total_dist += distance_between_points([0,0],package) #Drive from corner to the package

    index = closest(package, package_locations)

    pair = package_locations[index] #Finds the closest package

    package_locations.pop(index) #Deletes the paired package list

    total_dist += distance_between_points(package, pair) #Drive from package to pair

    order.append(pair) #Adds the pair to the order

    total_dist += distance_between_points(pair, [0,0]) #Drive from pair to corner

    total_dist += DISTANCE_TO_HOME #Drive from corner to home

if len(package_locations) == 1:
    #One left-over package
    total_dist += DISTANCE_TO_HOME
    total_dist += distance_between_points([0,0],package_locations[0]) * 2
    print "last package:", package_locations[0]
    order.append(package_locations[0])
    total_dist += DISTANCE_TO_HOME

print closest([0,0],[[1,1],[1,0],[0,1]])

print distance_between_points([5.0,0.0],[0.0,12.0])
print 'The order of the packages: '
print order
print '\nThe total distance that the robot traveled is', total_dist, 'yards.'
