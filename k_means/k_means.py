#!/usr/bin/env python
import mincemeat
import funcs
import sys

if (len(sys.argv) != 2):
	print ("Usage: python k_means.py <k>")
	sys.exit()

k = int(sys.argv[1])
	
# Get points
with open("points.txt") as f:
    content = f.readlines()
points = []
for p in content:
	x = float(p.strip().split()[0])
	y = float(p.strip().split()[1])
	points.append((x , y))

# Generate random k points
k_means = 	[(funcs.genRandom() , funcs.genRandom()) for i in range(k)]
print("Initial centers: ", k_means)

def mapfn(k, v):
	import shared as sh
	
	means = v[1]
	c = sh.findClosestCenter(v[0], means)
	yield c, v

def reducefn(k, vs):
	import shared as sh
		
	means = vs[0][1]
	points = [vs[i][0] for i in range(len(vs))]
	
	newCenter = sh.getAvg(points)
	return (newCenter, points)

# ------- Run mincemeat -------
improved = True
results = None
iterations = 0
while(improved):
	# Tweak data
	data = [(x, k_means) for x in points]
	datasource = dict(enumerate(data))
	
	s = mincemeat.Server()
	s.datasource = datasource
	s.mapfn = mapfn
	s.reducefn = reducefn

	results = s.run_server(password="pass")
	
	#Check for improvement in iteration
	improved = funcs.checkImprovement(results)
	
	#Update means
	k_means = [results[key][0] for key in results] + funcs.findMissingMeans(k_means, results)
	
	if(improved):
		print("improving iteration")
	else:
		print("none improving iteration")
		
	iterations += 1
	
# Setup final results
finalResults = dict()
for mean in k_means:
	if mean in results:
		finalResults[mean] = results[mean][1]
	else:
		finalResults[mean] = []

print("Convergence after ", iterations-1, " iterations. final results:")
for key, val in finalResults.items():
	print(key, " : ", val)
