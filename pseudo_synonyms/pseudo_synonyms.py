#!/usr/bin/env python
import mincemeat


def mapfn1(k, v):
    """
    Yields a pair where the key is the two words at the edges of the sentence,
    and the value is the middle word, which is a candidate to be a pseudo
    synonym.
    """
    d = v.split(" ")
    s = [x.strip() for x in d]
    yield tuple(sorted([s[0], s[2]])), s[1]


def reducefn1(k, vs):
    """Returns the values (pseudo-synonym candidates)"""
    return vs


def mapfn2(k, v):
    """Yields all pairs of pseudo-synonym candidates with the value 1"""
    for i in range(len(v)-1):
        first = v[i]
        for j in range(i+1, len(v)):
            second = v[j]
            yield tuple(sorted([first, second])), 1


def reducefn2(k, vs):
    """Returns the number of occurrences of the given pair"""
    return sum(vs)


if __name__ == "__main__":
    # Load the queries
    with open("queries.txt") as f:
        content = f.readlines()
    data = [x.strip() for x in content]
    datasource = dict(enumerate(data))

    # Run first MapReduce on mincemeat
    s = mincemeat.Server()
    s.datasource = datasource
    s.mapfn = mapfn1
    s.reducefn = reducefn1

    results = s.run_server(password="pass")

    # Prepare the data for the second MapReduce
    data = [results[key] for key in results]
    datasource = dict(enumerate(data))

    # Run second MapReduce on mincemeat
    s = mincemeat.Server()
    s.datasource = datasource
    s.mapfn = mapfn2
    s.reducefn = reducefn2

    results = s.run_server(password="pass")

    # Print the pseudo-synonyms
    for key in results:
        if results[key] > 1:
            print("%s - %s (%d)" % (key[0], key[1], results[key]))
