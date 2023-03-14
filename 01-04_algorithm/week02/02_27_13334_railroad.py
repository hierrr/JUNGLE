import sys
import heapq
input = sys.stdin.readline

n = int(input())
ho = list(sorted(list(map(int, input().split()))) for _ in range(n))
d = int(input())

cl = []
for c in ho:
    if c[1] - c[0] <= d:
        cl.append(c)
cl.sort(key=lambda x: x[1])

cnt = 0
heap = []
for c in cl:
    if not heap:
        heapq.heappush(heap, c)
    else:
        while heap and heap[0][0] < c[1] - d:
            heapq.heappop(heap)
        heapq.heappush(heap, c)
    cnt = max(cnt, len(heap))
print(cnt)
