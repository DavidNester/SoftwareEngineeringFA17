# /**************************************************RemoveLargest******************************************************
def consistent(pairs, freq, order, dist):
    """
    Selects pairs of packages if there is only 1 pair left with reference to that package
    Ensures that no package is missed
    :param pairs: dictionary with pairs of indexes of boxes as keys and distances as values
    :param freq: dictionary with number of references to each package left
    :param order: current order that packages have been selected
    :param dist: current distance that robot must travel for packages that have been selected
    :return: pairs: updated version of input with same name
    :return: freq: updated version of input with same name
    :return: order: updated version of input with same name
    :return: dist: updated version of input with same name
    """
    while 1 in freq.values():
        key = -1
        for k in freq:
            if freq[k] == 1:
                key = k
                break
        for k in pairs:
            if key in k:
                pair = k
                break
        dist += pairs[pair]
        order += pair
        order += ['--------------']
        remove = []
        for key in pairs:  # find entries that contain
            if not set(k).isdisjoint(key):
                remove += [key]
        for k in remove:  # remove entries
            for a in k:
                if freq[a] == 1:
                    del freq[a]
                else:
                    freq[a] -= 1
            del pairs[k]
    return pairs,freq,order,dist


def least_new(pairs, freq):
    """
    Removes largest distance from pairs until empty. Uses consistent() to select pairs when there is only one reference
    to a package remaining
    :param pairs: dictionary with pairs of indexes of boxes as keys and distances as values
    :param freq: dictionary with count of references to each box remaining
    :return: dist: distance traveled to pick up boxes
    :return: order: list of indices by order that they are taken
    """
    order = ['--------------']
    dist = 0
    if 1 in freq.values():
        pairs, freq, order, dist = consistent(pairs, freq, order, dist)
    while len(pairs) > 0:
        k = max(pairs, key=pairs.get)
        for i in k:
            freq[i] -= 1
        del pairs[k]
        pairs, freq, order, dist = consistent(pairs, freq, order, dist)
    return dist, order


def distance_remove_largest(locations):
    """
    Remove Largest Algorithm
    Adds length of trips back and forth to drop off site. Adds it to the distance traveled to and from boxes computed by
    from_origin. Travels 600 yards for every trip. Takes len(locations)/2 (rounding up) trips
    :param locations: list of locations of boxes
    :return: dist: total distance traveled by the robot
    :return: order: list of packages returned by index
    """
    pairs= make_pairs(locations)
    fr = len(locations)
    keys = list(range(len(locations)))
    if len(locations)%2 == 1:
        keys += [-1]
    else:
        fr -= 1
    freq = dict.fromkeys(keys,fr)
    dist, order = least_new(pairs,freq)
    return 600 * math.ceil(len(locations)/2.0) + dist, order
