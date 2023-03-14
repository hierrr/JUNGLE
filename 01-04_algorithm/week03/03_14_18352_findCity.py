import sys
from collections import deque
from heapq import heapify, heappush, heappop
inf = sys.maxsize
input = sys.stdin.readline

# bfs
def bfs(start):
    ret = []
    queue = deque()
    queue.append(start)
    vis[start] = 0
    while queue:
        i = queue.popleft()
        for j in graph[i]:
            if vis[j] == -1:
                vis[j] = vis[i] + 1
                if vis[j] == k:
                    ret.append(j)
                queue.append(j)
    return sorted(ret)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
# -1 for false, else distance
vis = [-1] * (n+1)
ret = bfs(x)
if not ret:
    print(-1)
else:
    print(*ret, sep="\n")

## dijkstra
#def dijkstra(start):
#    heap = []
#    heappush(heap, (start, 0))
#    dis[start] = 0
#    while heap:
#        node, tmp = heappop(heap)
#        if dis[node] < tmp:
#            continue
#        for next in graph[node]:
#            dist = dis[node] + next[1]
#            if dist < dis[next[0]]:
#                dis[next[0]] = dist
#                heappush(heap, (next[0], dist))
#
#n, m, k, x = map(int, input().split())
#graph = [[] for _ in range(n+1)]
#for _ in range(m):
#    u, v = map(int, input().split())
#    graph[u].append((v, 1))
#dis = [inf] * (n+1)
#
#dijkstra(x)
#ret = []
#for i in range(1, n+1):
#    if dis[i] == k:
#        ret.append(i)
#if not ret:
#    print(-1)
#else:
#    print(*ret, sep="\n")
