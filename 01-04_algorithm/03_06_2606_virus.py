import sys
input = sys.stdin.readline

def dfs(start):
    global cnt
    vis[start] = True
    for next in graph[start]:
        if not vis[next]:
            dfs(next)
            cnt += 1

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
vis = [False] * (n+1)
cnt = 0
dfs(1)
print(cnt)
