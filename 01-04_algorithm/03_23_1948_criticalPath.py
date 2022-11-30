import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    # time
    queue = deque()
    queue.append(start)
    while queue:
        i = queue.popleft()
        for j, t in graph[i]:
            indgr[j] -= 1
            time[j] = max(time[j], time[i] + t)
            if indgr[j] == 0:
                queue.append(j)
    # roads(bt)
    vis = [False] * (n+1)
    cnt = 0
    queue.append(end)
    while queue:
        i = queue.popleft()
        for j, t in rev_graph[i]:
            if time[i] - time[j] == t:
                cnt += 1
                if not vis[j]:
                    queue.append(j)
                    vis[j] = True
    return cnt

n = int(input())
m = int(input())
indgr = [0] * (n+1)
graph = [[] for _ in range(n+1)]
rev_graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))
    rev_graph[v].append((u, t))
    indgr[v] += 1
time = [0] * (n+1)
start, end = map(int, input().split())
cnt = topology_sort()
print(time[end], cnt, sep="\n")
