import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    dvi[v] = True
    dl.append(v)
    for i in range(1, n+1):
        if not dvi[i] and graph[v][i]:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    bvi[v] = True
    while queue:
        i = queue.popleft()
        bl.append(i)
        for j in range(1, n+1):
            if not bvi[j] and graph[i][j]:
                queue.append(j)
                bvi[j] = True

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
dvi, bvi = [False] * (n+1), [False] * (n+1)
dl, bl = [], []
dfs(v)
bfs(v)
print(*dl)
print(*bl)
