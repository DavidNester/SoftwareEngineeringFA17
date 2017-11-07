import math

def distance_between_points(pair1,pair2):
    return math.sqrt(((pair1[0]-pair2[0])**2 + (pair1[1] - pair2[1])**2)) #disance formula

def closest(p1, points):
    #returns the index of the point closest to p1.
    min_dist = distance_between_points(p1,points[0])
    index = 0
    for i in range(len(points)):
        if distance_between_points(p1,points[i]) < min_dist:
            min_dist = distance_between_points(p1,points[i])
            index = i
    return index
