# Intro to DS, HW #3 – Map Reduce

## K-Means algorithm
Our algorithm performs a few MapReduce iterations, where in each iteration:
- The Map function takes as input a point *p* and the current *k* centers,
finds the center *c* closest to the point, and yields *(c, p)*.
- The Reduce function takes as input a center *c* and a set of points *P* 
which chose *p* as a center, finds their mean *c'*, and returns (c', P).

The algorithm stops when none of the centers are updated, which means that
all the points picked the same center in this iteration.

### Usage

 The client's optional arguments are as follows:
  ```bash
  $ python k_means/k_means.py -h
  usage: k_means.py [-h] [-f FILENAME] [-k K]
  
  optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        File containing the points to cluster (default:
                        data.txt)
  -k K                  Number of clusters (default: 3)
  ```
  
  To run the server (each iteration requires another run of the server):
  ```bash
  $ python k_means/mincemeat.py -p pass localhost
  ```

## FindTriangles function
TODO: Describe the implementation

## Pseudo-synonyms detection algorithm
TODO: Describe the implementation
