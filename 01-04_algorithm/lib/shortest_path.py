import sys
from heapq import heapify, heappush, heappop
inf = sys.maxsize
input = sys.stdin.readline

## dijkstra for sssp(single source sp), O(V^2)
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
#vrtx, edge = map(int, input().split())
#graph = [[] for _ in range(vrtx+1)]
#for _ in range(edge):
#    u, v, d = map(int, input().split())
#    graph[u].append((v, d))
#vis = [False] * (vrtx+1)
#dis = [inf] * (vrtx+1)
#
#start, end = map(int, input().split())
#dijkstra(start)
#print(dis)

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

vrtx, edge = map(int, input().split())
graph = [[] for _ in range(vrtx+1)]
for _ in range(edge):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
dis = [inf] * (vrtx+1)

start, end = map(int, input().split())
dijkstra(start)
print(dis)

## bellman-ford for negative d, check cycle, O(VE)
#def bf(start):
#    dis[start] = 0
#    for i in range(vrtx):
#        for j in range(edge):
#            node, next, dist = graph[j]
#            if dis[node] != inf and dis[node] + dist < dis[next]:
#                dis[next] = dis[node] + dist
#                if i == vrtx-1:
#                    return False
#    return True
#
#vrtx, edge = map(int, input().split())
#graph = list(list(map(int, input().split())) for _ in range(edge))
#dis = [inf for _ in range(vrtx+1)]
#if bf(1):
#    for i in range(2, vrtx+1):
#        if dis[i] == inf:
#            print(0, end=" ")
#        else:
#            print(dis[i])
#else:
#    print("neg cycle xst")

## floyd-warshall for apsp(all pairs sp), O(V^3)
#def fw():
#    for i in range(1, vrtx+1):
#        for u in range(1, vrtx+1):
#            for v in range(1, vrtx+1):
#                graph[u][v] = min(graph[u][v], graph[u][i]+graph[i][v])
#
#vrtx, edge = map(int, input().split())
#graph = [[inf] * (vrtx+1) for _ in range(vrtx+1)]
#for i in range(1, vrtx+1):
#    for j in range(1, vrtx+1):
#        if i == j:
#            graph[i][j] = 0
#for _ in range(edge):
#    u, v, d = map(int, input().split())
#    graph[u][v] = min(graph[u][v], d)
#fw()
#for i in range(1, vrtx+1):
#    for j in range(1, vrtx+1):
#        if graph[i][j] != inf:
#            print(graph[i][j], end=" ")
#        else:
#            print(0, end=" ")
#    print()
