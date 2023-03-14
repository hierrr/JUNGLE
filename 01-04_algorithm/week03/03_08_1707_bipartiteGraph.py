import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# dfs
def dfs(start, color):
    vis[start] = color
    for next in graph[start]:
        if not vis[next]:
            if not dfs(next, -color):
                return False
        else:
            if vis[next] == vis[start]:
                return False
    return True

## bfs
#def bfs(start, color):
#    queue = deque()
#    queue.append(start)
#    vis[start] = color
#    while queue:
#        node = queue.popleft()
#        for next in graph[node]:
#            if not vis[next]:
#                vis[next] = -vis[node]
#                queue.append(next)
#            else:
#                if vis[next] == vis[node]:
#                    return False
#    return True

k = int(input())
for _ in range(k):
    vrtx, edge = map(int, input().split())
    graph = [[] for _ in range(vrtx+1)]
    for _ in range(edge):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    vis = [0] * (vrtx+1)
    flg = True
    for i in range(1, vrtx+1):
        if not vis[i]:
            if not dfs(i, 1):
#            if not bfs(i, 1):
                flg = False
                break
    print("YES" if flg else "NO")
