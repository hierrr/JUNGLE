import sys
from collections import defaultdict
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

## prim for dense graph, O(ElogV) >> O(V^2)
#def prim(graph, start):
#    vis[start] = True
#    cnd = graph[start]
#    heapify(cnd)
#    mst = []
#    ret = 0
#    while cnd:
#        w, u, v = heappop(cnd)
#        if not vis[v]:
#            vis[v] = True
#            mst.append((w, u, v))
#            ret += w
#            for edge in graph[v]:
#                if not vis[edge[2]]:
#                    heappush(cnd, edge)
#    return mst
#
#vrtx, edge = map(int, input().split())
#graph = defaultdict(list)
#for _ in range(edge):
#    u, v, w = map(int, input().split())
#    graph[u].append([w, u, v])
#    graph[v].append([w, v, u])
#vis = [False] * (vrtx+1)
#mst = prim(graph, 1)
#print(mst)

# kruskal for sparse graph, O(ElogV)
def find(prnt, x):
    if prnt[x] != x:
        prnt[x] = find(prnt, prnt[x])
    return prnt[x]
def union(prnt, u, v):
    u = find(prnt, u)
    v = find(prnt, v)
    if u < v:
        prnt[v] = u
    else:
        prnt[u] = v

vrtx, edge = map(int, input().split())
graph = []
for _ in range(edge):
    u, v, w = map(int, input().split())
    graph.append((w, u, v))
graph.sort()
prnt = [0] * (vrtx+1)
for i in range(1, v+1):
    prnt[i] = i
mst = []
ret = 0
for _ in graph:
    w, u, v = _
    if find(prnt, u) != find(prnt, v):
        union(prnt, u, v)
        mst.append((w, u, v))
        ret += w
print(ret)
print(mst)
