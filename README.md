# Intro to DS, HW #3 – Map Reduce
Submitted by Ron Kabas (311504484) and Eitan-Hai Mashiah (206349045).

In each section, run the client first from the appropriate folder (using 
the command in that section), and then in another terminal from the same folder, 
run the server with the following command:
```bash
$ python mincemeat.py -p pass localhost
```

### K-Means
The program loads the points from the `points.txt` file (located in the 
`k_means` folder). It performs a few MapReduce iterations, and stops when none of
the centers are updated, which means that all the points picked the same center in
that iteration. Finally, it prints the resulting clusters alongside their centers. 

To run the client:
```bash
$ python k_means.py [-h] [-k K]
```
where K is the number of required clusters (default: 3). In addition, note that 
each iteration requires another run of the server.

## FindTriangles
The program loads the graph represented by its adjacency list from the `grpah.txt`
file (located in the `find_triangle` folder), and prints all the triangles 
(cliques of size 3) in the graph.

To run the client:
```bash
$ python find_triangles.py
```

## Pseudo synonyms
The program loads the 3-word queries from the `queries.txt` file (located in the
`pseudo_synonyms` folder), and prints all the pseudo-synonyms from them.

To run the client:
```bash
$ python find_triangles.py
```

Note that since this task requires two MapReduce stages, the server needs to be run 
twice sequentially.
