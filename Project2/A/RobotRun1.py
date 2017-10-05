from calculations import distance_between_points
import math

package_locations = [[1.5, 11], [6,  11], [7, 11], [4,  10], [6.5, 9], [8, 9], \
                     [3, 8], [2, 7], [7.5, 6], [4, 5], [2.5, 4], [6, 4], \
                     [8, 4], [2, 2], [3, 2], [9, 2], [1, 1], [2, 1], [6, 1], \
                     [10, 1], [1, 6] ]

def between(locations):
    pairs = {}
    for i in range(len(locations)):
        for j in range(len(locations)):
            if i != j:
                pairs[(i,j)] = distance_between_points(i,j)

def from_origin(locations):
    distance = 0
    for location in locations:
        distance += distance_between_points([0,0],location)
    return distance + between(locations)

def distance(locations):
    return 600*math.ceiling(len(locations)/2) + from_origin(locations)

if __name__ == "__main__":
    print "This program prints some shit"
    print package_locations
    print distance_between_points([1.0,1.0],[6.0,5.0])
