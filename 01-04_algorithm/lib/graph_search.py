import sys
from collections import deque
input = sys.stdin.readline

# dfs(recursive)
def dfs_rec(v):
    if not vis[v]:
        vis[v] = True
        ret.append(v)
        for i in graph[v]:
            dfs_rec(i)    

# dfs(stack)
def dfs(v):
    ret = []
    vis = [False] * (n+1)
    stack = []
    stack.append(v)
    while stack:
        i = stack.pop()
        if not vis[i]:
            vis[i] = True
            ret.append(i)
            for j in graph[i]:
                if not vis[j]:
                    stack.append(j)
    return ret

# bfs(queue)
def bfs(v):
    ret = []
    vis = [False] * (n+1)
    queue = deque()
    queue.append(v)
    while queue:
        i = queue.popleft()
        if not vis[i]:
            vis[i] = True
            ret.append(i)
            for j in graph[i]:
                if not vis[j]:
                    queue.append(j)
    return ret

n, m, v = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# dfs(recursive)
ret = []
vis = [False] * (n+1)
dfs_rec(v)
print(*ret)
# dfs(stack)
print(*dfs(v))
# bfs(queue)
print(*bfs(v))
