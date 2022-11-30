import sys
from collections import deque
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

# dfs
def dfs(start):
    vis[start] = True
    for next in graph[start]:
        if not vis[next]:
            dfs(next)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
vis = [False] * (n+1)
cnt = 0
for i in range(1, n+1):
    if not vis[i]:
        if not graph[i]:
            vis[i] = True
            cnt += 1
        else:
            dfs(i)
            cnt += 1
print(cnt)

## bfs
#def bfs(start):
#    queue = deque()
#    queue.append(start)
#    vis[start] = True
#    while queue:
#        node = queue.popleft()
#        for next in graph[node]:
#            if not vis[next]:
#                vis[next] = True
#                queue.append(next)
#
#n, m = map(int, input().split())
#graph = [[] for _ in range(n+1)]
#for _ in range(m):
#    u, v = map(int, input().split())
#    graph[u].append(v)
#    graph[v].append(u)
#vis = [False] * (n+1)
#cnt = 0
#for i in range(1, n+1):
#    if not vis[i]:
#        if not graph[i]:
#            vis[i] = True
#            cnt += 1
#        else:
#            bfs(i)
#            cnt += 1
#print(cnt)
