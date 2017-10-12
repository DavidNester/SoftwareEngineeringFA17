"""
Author: David Nester
Date: 10.6.17
Module with functions useful to robot package pickup simulation.
"""
def distance_between_points(x, y):
    """
    Euclidean distance between two points, x and y
    :param x: point 1
    :param y: point 2
    :return: Euclidean distance
    """
    return ((float(x[0]) - float(y[0]))**2 + (float(x[1]) - float(y[1]))**2)**.5


def make_pairs(locations):
    """
    Creates dictionary of pairs of indices of boxes as keys and distances between them as values
    :param locations: list of locations of boxes
    :return: pairs: dictionary with pairs of indices of boxes as keys and distances as values
    """
    pairs = {}
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            if i != j:
                pairs[i, j] = distance_between_points(locations[i], locations[j]) + \
                              distance_between_points([0,0],locations[i]) + distance_between_points([0,0],locations[j])
        if len(locations) % 2 == 1:  # if odd number of boxes, add entry for trip from origin to box (only one chosen)
            pairs[i, -1] = 2 * distance_between_points([0, 0], locations[i])
    return pairs
