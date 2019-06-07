#!/usr/bin/env python
import mincemeat

def isFullClique(d):
	for key,val in d.items():
		if(val < n-1):
			return False;
	return True
	
# Get points
with open("graph.txt") as f:
    content = f.readlines()
data = [x.strip() for x in content]
datasource = dict(enumerate(data))


def mapfn(k, v):	
	d = v.split("->")
	src = d[0].strip()
	adjecent = set(d[1].strip().split(" "))
	
	if(adjecent == {''}):
		yield src, '' 
	
	for w in adjecent:
		yield src, w

def reducefn(k, vs):	
	if(vs[0] == ''):
		return 0
		
	s = set(vs)
		
	return len(s)

# ------- Run mincemeat -------
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="pass")

n = len(results)

str = 'Graph is a full clique: '
if isFullClique(results):
	print(str + 'Yes')
else:
	print(str + 'No')
