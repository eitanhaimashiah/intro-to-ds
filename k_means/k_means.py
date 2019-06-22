#!/usr/bin/env python
import argparse
import mincemeat
import random


def mapfn(k, v):
    """Finds the center closest to the point among the given centers"""
    point = v[0]
    centers = v[1]
    min_dist = 2  # the maximum squared distance between points in [0,1]x[0,1]
    min_center = centers[0]
    for center in centers:
        dist = (center[0] - point[0])**2 + (center[1] - point[1])**2  # squared distance
        if dist < min_dist:
            min_dist = dist
            min_center = center

    yield min_center, v


def reducefn(k, vs):
    """Returns the mean of the given points"""
    points = [v[0] for v in vs]
    sum_x, sum_y = 0, 0
    for x, y in points:
        sum_x += x
        sum_y += y
    n = len(points)
    new_center = (float(sum_x)/n, float(sum_y)/n)
    return new_center, points


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", default=3, help="Number of clusters (default: 3)")
    args = parser.parse_args()

    # Load the points
    points = []
    with open("points.txt") as f:
        content = f.readlines()
    for line in content:
        point = line.strip().split()
        points.append((float(point[0]), float(point[1])))

    # Init with k random centers
    centers = [(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)) for i in range(args.k)]
    print("Initial centers: ", centers)

    # Run MapReduce on mincemeat
    iterations = 0
    keep_going = True
    results = None
    while keep_going:
        # Adjust data to mincemeat format
        data = [(point, centers) for point in points]
        datasource = dict(enumerate(data))

        # Create a server
        s = mincemeat.Server()
        s.datasource = datasource
        s.mapfn = mapfn
        s.reducefn = reducefn

        results = s.run_server(password="pass")

        # If there is a center that was updated, continue to further iteration
        keep_going = False
        for key in results:
            if results[key][0] != key:
                keep_going = True

        # Find centers that weren't selected by any point
        unselected_centers = [center for center in centers if center not in results]

        # Update centers
        centers = [results[key][0] for key in results] + unselected_centers

        print("Finished iteration", iterations)
        iterations += 1

    # Print final results
    print("Convergence after", iterations-1, "iterations. Final results:")
    for center in centers:
        if center in results:
            print(center, ":", results[center][1])
        else:
            print(center, ":", [])
