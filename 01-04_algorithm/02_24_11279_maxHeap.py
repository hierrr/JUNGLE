import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x:
        # heappush(heap, (priority, value))
        heapq.heappush(heap, (-x, x))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
