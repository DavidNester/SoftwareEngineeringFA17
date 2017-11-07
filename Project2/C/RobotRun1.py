"""
Author: David Nester
Date: 11.1.17
PYTHON 2.7
Module to simulate a robot picking up packages. Solution is not necessarily optimal.
"""
from calculations import make_pairs, make_pairs_new, distance_between_points, sort, distance_without_front_axle_limitation
import math

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
            order += [k[0],'None']
        else:
            order += k
        remove = []
        for key in pairs:  # find entries that have same same packages as the one selected
            if k[0] == key[0] or k[1] == key[1]:
                remove += [key]
        for k in remove:  # remove entries
            del pairs[k]
        order += ['--------------']  # added to signify a trip back to the drop-off site
    return dist, order


def distance_take_smallest(first, second):
    """
    Adds length of trips back and forth to drop off site. Adds it to the distance traveled to and from boxes computed by
    from_origin. Travels 600 yards for every trip. Takes len(locations)/2 (rounding up) trips
    :param first: list of locations that are picked up first
    :param second: list of locations that are picked up second
    :return: dist: total distance traveled by the robot
    :return: order: list of packages returned by index
    """
    pairs = make_pairs_new(first,second)
    dist, order = least(pairs)
    for p in first:
        dist += distance_between_points([0, 0], p)
    return 600 * len(first) + dist, order


if __name__ == "__main__":
    package_locations = [[1.5, 11], [6, 11], [7, 11], [4, 10], [6.5, 9], [8, 9],
                         [3, 8], [2, 7], [7.5, 6], [4, 5], [2.5, 4], [6, 4],
                         [8, 4], [2, 2], [3, 2], [9, 2], [1, 1], [2, 1], [6, 1],
                         [10, 1], [1, 6]]
    #ALGORITHM DESCRIPTION:
    """
    The algorithm works the same way as part A except that it makes the pairs differently. It starts by
    sorting the list by distance and then makes two lists, the first half of the items (those closest to the origin) 
    and the rest and makes pairs so that no location is paired with an element in its same set. Then it performs
    the same algorithm as before (selecting the smallest distance until empty).
    Technically, it would be better to take each package individually and put it on the back but I assumed that would
    not be a desired solution given the triviality of the solution. It could be useful to put a cost on front axle
    distance and a cost on normal distance to get an idea of how to optimally trade them off.     
    """
    sorted_locations = sort(package_locations)
    mid = len(sorted_locations) / 2
    second_packages = sorted_locations[0:mid]
    first_packages = sorted_locations[mid:]
    dist, order = distance_take_smallest(first_packages, second_packages)
    front_axle_distance = 0
    for p in second_packages:
        front_axle_distance += distance_between_points(p, [0, 0])
    dist += front_axle_distance

    print 'Front Axle Distance: ' + str(front_axle_distance)
    print 'Total Distance: ' + str(dist)
    old_dist, old_ord = distance_without_front_axle_limitation(package_locations)
    print 'Normal Best Distance: ' + str(old_dist)
    old_front_dist = 0
    for i in range(len(old_ord)):
        if not isinstance(old_ord[i-1],str) and not isinstance(old_ord[i],str):
            old_front_dist += distance_between_points(package_locations[old_ord[i]],[0,0])
    print 'Normal Distance On Front Axle: ' + str(old_front_dist)

    true_ord = 1  # numbers order that packages are returned because order contains spacers
    while len(order) != 0:
        print order.pop(0)
        print str(true_ord) + ' : ' + str(first_packages[order.pop(0)])
        true_ord += 1
        next_item = order.pop(0)
        if isinstance(next_item, str):
            print next_item
        else:
            print str(true_ord) + ' : ' + str(second_packages[next_item])
            true_ord += 1
        if len(order) == 1:
            print order.pop(0)