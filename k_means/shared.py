#!/usr/bin/env python
	
def getDist(a,b):
	return ( (a[0] - b[0])**2 + (a[1] - b[1])**2 )
	
def findClosestCenter(x, means):
	minPoint = means[0]
	minDist = 2
	
	for i in range(len(means)):
		dist = getDist(means[i], x)
		if(dist < minDist):
			minDist = dist
			minPoint = means[i]
			
	return minPoint
	
def getAvg(arr):
	n = len(arr)
	x = 0
	y = 0
	
	for i in range(n):
		x += arr[i][0]
		y += arr[i][1]
	
	return (x / n , y / n)
	
