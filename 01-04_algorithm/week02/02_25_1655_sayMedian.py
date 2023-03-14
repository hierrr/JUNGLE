import sys
import heapq
input = sys.stdin.readline

n = int(input())
# lower: max_heap, upper: min_heap
l_heap, u_heap = [], []
l_cnt, u_cnt = 0, 0

for _ in range(n):
    tmp = int(input())
    # init or tmp <= median(l_heap[0][1])
    if not l_cnt or tmp <= l_heap[0][1]:
        heapq.heappush(l_heap, (-tmp, tmp))
        l_cnt += 1
        if l_cnt > u_cnt+1:
            tr = heapq.heappop(l_heap)
            heapq.heappush(u_heap, tr[1])
            l_cnt -= 1
            u_cnt += 1
    # tmp > median
    else:
        heapq.heappush(u_heap, tmp)
        u_cnt += 1
        if l_cnt < u_cnt:
            tr = heapq.heappop(u_heap)
            heapq.heappush(l_heap, (-tr, tr))
            l_cnt += 1
            u_cnt -= 1
    print(l_heap[0][1])
