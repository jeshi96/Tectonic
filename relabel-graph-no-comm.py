#!/usr/bin/python

import sys
import pickle

graph = open(sys.argv[1])
#communities = open(sys.argv[2])
out_graph = open(sys.argv[2], 'w')
#out_communities = open(sys.argv[4], 'w')

out_map = open(sys.argv[3], 'wb')


vid = 0
vid_map = {}
for line in graph:
    if line[0] == '#':
        continue
    e = list(line.split())
    e[0] = int(e[0])
    e[1] = int(e[1])
    if(len(e)==0):
        continue
    if not e[0] in vid_map:
        vid_map[e[0]] = vid
        vid += 1
    if not e[1] in vid_map:
        vid_map[e[1]] = vid
        vid += 1

n = vid
edges = [[] for i in range(n)]

graph.seek(0)
for line in graph:
    if line[0] == '#':
        continue

    e = list(line.split())
    e[0] = int(e[0])
    e[1] = int(e[1])
    if(len(e)==0):
        continue
    u = vid_map[e[0]]
    v = vid_map[e[1]]
    edges[min(u, v)].append(max(u, v))
graph.close()

for l in edges:
    out_graph.write(' '.join(map(str, l)) + '\n')
out_graph.close()

pickle.dump(vid_map, out_map)
out_map.close()

print(str(n))

#out_communities.write(str(n) + '\n')
#for line in communities:
#    l = []
#    for i in map(int, line.split()):
#        l.append(vid_map[i])
#    out_communities.write(' '.join(map(str, l)) + '\n')
#out_communities.close()
