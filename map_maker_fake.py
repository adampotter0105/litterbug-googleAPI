# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 20:32:30 2019

@author: adamp
"""
import random as r

size = 20
#make nodes
nodes=[]
for x in range(size):
    for y in range(size):
        nodes.append([x+r.random(),y+r.random()])
nodes = [[round(x*100),round(y*100)] for [x,y] in nodes]
#make edges
edges=[]
for i in range(size-1):
    for j in range(size-1):
        edges.append([j+20*i,j+20*i+1])
        edges.append([j+20*i,j+20*(i+1)])

#make litter
weights=[]
res = 4
for i in range(len(edges)):
    weights.append([])
    for j in range(res):
        weights[i].append(r.randint(0,5))
        
print("Nodes: ")
print(nodes)
print("Edges: ")
print(edges)
print("Litter: ")
print(weights)