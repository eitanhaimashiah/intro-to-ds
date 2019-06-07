#!/usr/bin/env python
import random


def genRandom():
	return random.uniform(0.0 , 1.0)
	
def checkImprovement(results):
	c = 0
	for key in results:
		if(results[key][0] != key):
			return True
		
	return False

# In case no point chose the centroid,
# add him as is back to the means
def findMissingMeans(oldMeans, results):
	missing = []
	for mean in oldMeans:
		if not(mean in results):
			missing.append(mean)
			
	return missing