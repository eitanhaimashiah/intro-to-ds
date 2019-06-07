#!/usr/bin/env python
import mincemeat
	
# Get input
with open("input.txt") as f:
    content = f.readlines()
data = [x.strip() for x in content]
datasource = dict(enumerate(data))


def initMap(k, v):	
	d = v.split(" ")
	s = [x.strip() for x in d]
	
	lst = sorted([s[0],s[2]], key=str.lower)
	yield (lst[0],lst[1]) , s[1]

def initReduce(k, vs):	
	return vs

# ------- Run first MR -------
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = initMap
s.reducefn = initReduce

results = s.run_server(password="pass")
# print (results)

data = [results[key] for key in results]
datasource = dict(enumerate(data))

def synonymsMap(k, v):	
	# Generate all pairs of words in v
	pairs = []
	for i in range(len(v)):
		for j in range(i+1, len(v)):
			pairs.append((v[i], v[j]))

	
	for p in pairs:
		lst = sorted(p, key=str.lower)
		yield (lst[0], lst[1]), 1
		
def synonymsReduce(k, vs):
	return sum(vs)
	
# ------- Run second MR -------
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = synonymsMap
s.reducefn = synonymsReduce

results = s.run_server(password="pass")
# print (results)

for key in results:
	if (results[key] > 1):
		print(key[0] + " - " + key[1] + " (%d)" % results[key])
	
	
	
	
