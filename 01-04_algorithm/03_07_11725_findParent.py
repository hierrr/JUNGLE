import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    vis[start] = True
    for next in graph[start]:
        if not vis[next]:
            ret[next] = start
            dfs(next)

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
vis = [False] * (n+1)
ret = [0] * (n+1)
dfs(1)
print(*ret[2:], sep="\n")
