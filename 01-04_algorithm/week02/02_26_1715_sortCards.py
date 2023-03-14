import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = list(int(input()) for _ in range(n))
heapq.heapify(heap)

cnt = 0
for _ in range(n-1):
    tmp = heapq.heappop(heap) + heapq.heappop(heap)
    cnt += tmp
    if not heap:
        break
    heapq.heappush(heap, tmp)
print(cnt)
