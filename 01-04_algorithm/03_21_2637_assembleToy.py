import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    queue = deque()
    for i in range(1, n+1):
        if indgr[i] == 0:
            queue.append(i)
    while queue:
        now = queue.popleft()
        for next, nums in graph[now]:
            # basic part
            if cmpnt[now].count(0) == n+1:
                cmpnt[next][now] += nums
            # middle part
            else:
                for i in range(1, n+1):
                    cmpnt[next][i] += cmpnt[now][i] * nums
            indgr[next] -= 1
            if indgr[next] == 0:
                queue.append(next)

n = int(input())
m = int(input())
indgr = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    indgr[x] += 1
cmpnt = [[0] * (n+1) for _ in range(n+1)]

topology_sort()
for i in range(1, n+1):
    if cmpnt[n][i]:
        print(i, cmpnt[n][i])
