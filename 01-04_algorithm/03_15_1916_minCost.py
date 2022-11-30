import sys
from heapq import heapify, heappush, heappop
inf = sys.maxsize
input = sys.stdin.readline

## dijkstra, O(V^2)
#def shortest():
#    min = inf
#    idx = 0
#    for i in range(1, vrtx+1):
#        if not vis[i] and dis[i] < min:
#            min = dis[i]
#            idx = i
#    return idx
#def dijkstra(start):
#    dis[start] = 0
#    vis[start] = True
#    for path in graph[start]:
#        dis[path[0]] = min(dis[path[0]], path[1])
#    for _ in range(vrtx-1):
#        now = shortest()
#        vis[now] = True
#        for next in graph[now]:
#            dist = dis[now] + next[1]
#            if dist < dis[next[0]]:
#                dis[next[0]] = dist
#
#vrtx = int(input())
#edge = int(input())
#graph = [[] for _ in range(vrtx+1)]
#for _ in range(edge):
#    u, v, d = map(int, input().split())
#    graph[u].append((v, d))
#start, end = map(int, input().split())
#vis = [False] * (vrtx+1)
#dis = [inf] * (vrtx+1)
#
#dijkstra(start)
#print(dis[end])

# dijkstra with priority queue(heap), O((V+E)logV)
def dijkstra(start):
    heap = []
    heappush(heap, (start, 0))
    dis[start] = 0
    while heap:
        node, tmp = heappop(heap)
        if dis[node] < tmp:
            continue
        for next in graph[node]:
            dist = dis[node] + next[1]
            if dist < dis[next[0]]:
                dis[next[0]] = dist
                heappush(heap, (next[0], dist))

vrtx = int(input())
edge = int(input())
graph = [[] for _ in range(vrtx+1)]
for _ in range(edge):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
dis = [inf] * (vrtx+1)

start, end = map(int, input().split())
dijkstra(start)
print(dis[end])
