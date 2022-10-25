#!/usr/bin/python

import sys

graph = open(sys.argv[1])
clusters = open(sys.argv[2])
out_clusters = open(sys.argv[3], 'w')


vid = 0
vid_map = {}
for line in graph:
    if line[0] == '#':
        continue

    e = map(int, line.split())
    if not e[0] in vid_map:
        vid_map[e[0]] = vid
        vid += 1
    if not e[1] in vid_map:
        vid_map[e[1]] = vid
        vid += 1

n = vid
edges = [[] for i in range(n)]

inv_vid_map = {v: k for k, v in vid_map.iteritems()}

for line in clusters:
    l = []
    for i in map(int, line.split()):
        l.append(inv_vid_map[i])
    out_clusters.write('\t'.join(map(str, l)) + '\n')
out_clusters.close()
clusters.close()