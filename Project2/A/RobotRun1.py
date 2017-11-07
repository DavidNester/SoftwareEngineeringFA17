"""
Author: David Nester
Date: 10.10.17
Module to simulate a robot picking up packages. Solution is not necessarily optimal.
"""
from calculations import make_pairs, distance_between_points
import math


# /**************************************************TakeSmallest*******************************************************
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


def distance_take_smallest(locations):
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


# /**************************************************Recursive**********************************************************
def rem(pair,pairs):
    """
    Removes pair from pairs and any entries in pairs that have indices in common with pair
    :param pair: pair to be removed
    :param pairs: dictionary of pairs of indices
    :return: updated pairs with pair removed
    """
    remove = []
    for key in pairs:  # find entries that contain common indices
        if not set(pair).isdisjoint(key):
            remove += [key]
    for k in remove:  # remove entries
        del pairs[k]
    return pairs


def recursive(pairs,ind,visited,l):
    """
    Recursive method to get shortest distance combination of packages to be picked up
    :param pairs: dictionary with pairs of indexes of boxes as keys and distances as values
    :param ind: index to be selected for this recursive step
    :param visited: indices that have been used prior to this
    :param l: number of packages - used to decide what indices are left to check
    :return: minimum possible distance
    """
    if len(pairs) == 1:  # return last length if only one pair left
        for p in pairs:
            return pairs[p]
    pos_key = []
    for pair in pairs: # get all keys containing ind
        if ind in pair:
            pos_key += [pair]
    pos_pair = []
    for key in pos_key: # get list of tuples with length of pair and pairs with pair removed
        pos_pair += [(pairs[key],rem(key, pairs.copy()),key)]
    pos_lengths = []
    for pair in pos_pair:
        # figure out potential new ind values for next recursion level
        # add indices to visited
        temp_visited = visited.copy() + list(pair[2])
        next_ind = list(range(l))
        for i in temp_visited:
            if i != -1:
                next_ind.remove(i)
        pos_lengths += [pair[0] + recursive(pair[1],next_ind[0],temp_visited,l)]  # get list of possible distances
    return min(pos_lengths) # return shortest length out of all possible with choices for that index

def distance_recursive(locations):
    """
    Adds length of trips back and forth to drop off site. Adds it to the distance traveled to and from boxes computed by
    from_origin. Travels 600 yards for every trip. Takes len(locations)/2 (rounding up) trips
    :param locations: list of locations of boxes
    :return: dist: total distance traveled by the robot
    :return: order: list of packages returned by index
    """
    pairs = make_pairs(locations)
    dist = recursive(pairs,0,[],len(locations))
    return 600 * math.ceil(len(locations)/2.0) + dist

# /*********************************************************************************************************************

def main():
    """
    Function that runs all three algorithms and prints the optimal order and distance
    """
    if len(package_locations) < 15:
        optimal_distance = distance_recursive(package_locations)
        print('Optimal Distance:',round(optimal_distance,2),'yards')
    else:
        print('Optimal Distance takes too long to calculate (O(n!))')
    distance, order = distance_take_smallest(package_locations)
    print('Take Smallest:',round(distance,2),'yards')

    for package in package_locations:
        distance += distance_between_points([0,0],package)

    true_ord = 1  # numbers order that packages are returned because order contains spacers
    for i in range(len(order)):
        if isinstance(order[i],str):  # if entry is '----' then just print it
            print(order[i])
        else:
            print(true_ord,':',package_locations[order[i]])
            true_ord += 1

if __name__ == "__main__":
    print('\nSimulates a robot picking up packages and dropping them off. The robot starts at the drop off point and \n'
          'travels to the entrance of a room 300 yards away. The robot knows the coordinates of each package relative\n'
          'to the entrance (treated as the origin). The robot can pick up two packages at once. This program computes\n'
          'the distance traveled by the robot and gives the order that the packages are picked up and dropped off.')
    print('\nBrute Force: Given a dictionary of pairs with the distance required to pick up the pairs as values, the\n'
          'brute force method takes all pairs containing one package. It takes the length of the path required to\n'
          'pick up those packages and adds it to the shortest possible set of pairs of the remaining pairs.')
    print('TODO: Return optimal order through brute force')
    print('\nTake Shortest: Given a dictionary of pairs with the distance required to pick up the pairs as values,\n'
          'the algorithm takes the shortest pair and then removes all pairs that have indices in common. Repeats\n'
          'until list of pairs is empty.')
    print('\nBrute Force returns the optimal distance but does not return order and is set not to run when the number\n'
          'of packages gets large because it is not a quick algorithm O(n!). Take Shortest runs quickly but is not\n'
          'necessarily optimal.\n\n\n')
    package_locations = [[1.5, 11], [6, 11], [7, 11], [4, 10], [6.5, 9], [8, 9],
                         [3, 8], [2, 7], [7.5, 6], [4, 5], [2.5, 4], [6, 4],
                         [8, 4], [2, 2], [3, 2], [9, 2], [1, 1], [2, 1], [6, 1],
                         [10, 1], [1, 6]]
    package_locations = [[1.5, 11], [6, 11], [7, 11], [4, 10], [6.5, 9], [8, 9],
                         [3, 8], [2, 7], [7.5, 6], [4, 5],[2.5,4]]
    main()