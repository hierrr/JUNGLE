import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def topology_sort():
    ret = [0] * (n+1)
    heap = []
    for i in range(1, n+1):
        if indgr[i] == 0:
            # max_heap
            heappush(heap, -i)
    tmp = n
    while heap:
        j = -heappop(heap)
        ret[j] = tmp
        for k in graph[j]:
            indgr[k] -= 1
            if indgr[k] == 0:
                heappush(heap, -k)
        tmp -= 1
    return ret

n = int(input())
indgr = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for v in range(1, n+1):
    tmp = list(map(int, list("0" + input().rstrip())))
    # rev edge
    for u in range(1, n+1):
        if tmp[u] == 1:
            graph[u].append(v)
            indgr[v] += 1
ret = topology_sort()
if ret.count(0) > 1:
    print(-1)
else:
    print(*ret[1:])
