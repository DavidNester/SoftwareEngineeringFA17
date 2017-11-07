import math
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


def make_pairs_new(first,second):
    """
    Creates dictionary of pairs of indices of boxes as keys and distances between them as values
    :param locations: list of locations of boxes
    :return: pairs: dictionary with pairs of indices of boxes as keys and distances as values
    """
    pairs = {}
    for f in range(len(first)):
        for s in range(len(second)):
            pairs[f, s] = distance_between_points(first[f], second[s])
        if len(first) > len(second):  # if odd number of boxes, add entry for trip from origin to box (only one chosen)
            pairs[f, -1] =  distance_between_points([0, 0], first[f])
    return pairs

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
            pairs[i, -1] =  distance_between_points([0, 0], locations[i]) * 2
    return pairs


def sort(locations):
    dic = {}
    for location in locations:
        location = (location[0],location[1])
        dic[location] = distance_between_points([0,0],location)
    sorted_list = []
    for key, value in sorted(dic.iteritems(), key=lambda (k, v): (v, k)):
        sorted_list += [key]
    return sorted_list


# /**************************************************Old Way*******************************************************
def least(pairs):
    """
    Returns order of boxes taken and the total distance traveled between them.
    :param pairs: dictionary with pairs of indexes of boxes as keys and distances as values
    :return: dist: distance traveled between the boxes
    :return: order: list of indices by order that they are taken
    """
    order = ['--------------']
    dist = 0
    while len(pairs) > 0:
        k = min(pairs, key=pairs.get)
        dist += pairs[k]
        if -1 in k:  # check if pair contains length (used as dummy if only going to one package)
            order += [k[0]]
        else:
            order += k
        remove = []
        for key in pairs:  # find entries that have same same packages as the one selected
            if not set(k).isdisjoint(key):
                remove += [key]
        for k in remove:  # remove entries
            del pairs[k]
        order += ['--------------']  # added to signify a trip back to the drop-off site
    return dist, order


def distance_without_front_axle_limitation(locations):
    """
    Adds length of trips back and forth to drop off site. Adds it to the distance traveled to and from boxes computed by
    from_origin. Travels 600 yards for every trip. Takes len(locations)/2 (rounding up) trips
    :param locations: list of locations of boxes
    :return: dist: total distance traveled by the robot
    :return: order: list of packages returned by index
    """
    pairs = make_pairs(locations)
    dist, order = least(pairs)
    return 600 * math.ceil(len(locations)/2.0) + dist, order
