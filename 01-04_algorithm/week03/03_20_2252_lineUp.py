import sys
from collections import deque
input = sys.stdin.readline

# topology_sort, sort dag to linear by in-degree, O(V+E)
## dfs(rec)
#def topology_sort(graph):
#    def dfs(v, ret):
#        vis[v] = True
#        for u in graph[v]:
#            if not vis[u]:
#                dfs(u, ret)
#        ret.append(v)
#    ret = []
#    vis = [False] * (vrtx+1)
#    for i in range(1, vrtx+1):
#        if not vis[i]:
#            dfs(i, ret)
#    return ret[::-1]
#
## dfs(stack)
#def topology_sort(graph, indgr):
#    ret = []
#    stack = []
#    for i in range(1, vrtx+1):
#        if indgr[i] == 0:
#            stack.append(i)
#    while stack:
#        j = stack.pop()
#        ret.append(j)
#        for k in graph[j]:
#            indgr[k] -= 1
#            if indgr[k] == 0:
#                stack.append(k)
#    return ret

# bfs(queue)
def topology_sort(graph, indgr):
    ret = []
    queue = deque()
    for i in range(1, vrtx+1):
        if indgr[i] == 0:
            queue.append(i)
    while queue:
        j = queue.popleft()
        ret.append(j)
        for k in graph[j]:
            indgr[k] -= 1
            if indgr[k] == 0:
                queue.append(k)
    return ret

vrtx, edge = map(int, input().split())
indgr = [0] * (vrtx+1)
graph = [[] for _ in range(vrtx+1)]
for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    indgr[v] += 1
#print(topology_sort(graph))
print(topology_sort(graph, indgr))
