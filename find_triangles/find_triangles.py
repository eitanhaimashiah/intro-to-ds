#!/usr/bin/env python
import mincemeat


def mapfn(k, v):
    """
    If the given node has less than 2 neighbors, it cannot be a part of a triangle,
    and thus yields the node with the value 0. Otherwise, yields all triplets
    composed of the node and two of its neighbors, with the value 1.
    """
    d = v.split("->")
    first = d[0].strip()
    neighbors = list(d[1].strip().split(" "))
    n_neighbors = len(neighbors)

    # If the node has less than 2 neighbors, yield the node with the value 0
    if n_neighbors < 2:
        yield first, 0

    # Yields all triplets composed of the node and two of its neighbors, with the value 1
    for i in range(n_neighbors-1):
        second = neighbors[i]
        for j in range(i+1, n_neighbors):
            third = neighbors[j]
            yield tuple(sorted([first, second, third])), 1


def reducefn(k, vs):
    """
    Returns whether the given triplet is a triangle in the graph. This is done by
    counting the occurrences of the triplet - if there are 3 occurrences, that means
    that all its nodes are connected to each other, and hence it is a clique of size 3.
    """
    if sum(vs) == 3:
        return True
    return False


if __name__ == "__main__":
    # Load the graph
    with open("graph.txt") as f:
        content = f.readlines()
    data = [x.strip() for x in content]
    datasource = dict(enumerate(data))

    # Run MapReduce on mincemeat
    s = mincemeat.Server()
    s.datasource = datasource
    s.mapfn = mapfn
    s.reducefn = reducefn

    results = s.run_server(password="pass")

    # Print all the triangles in the graph
    for key in results:
        if results[key]:
            print(key)
