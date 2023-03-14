import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline

## bfs
#def bfs():
#    dr = [0, 1, 0, -1]
#    dc = [1, 0, -1, 0]
#    queue = deque()
#    queue.append((0, 0))
#    vis[0][0] = 0
#    while queue:
#        r, c = queue.popleft()
#        if r == n-1 and c == n-1:
#            return vis[r][c]
#        for i in range(4):
#            nr = r + dr[i]
#            nc = c + dc[i]
#            if -1<nr<n and -1<nc<n and vis[nr][nc] == -1:
#                if room[nr][nc]:
#                    queue.appendleft((nr, nc))
#                    vis[nr][nc] = vis[r][c]
#                else:
#                    queue.append((nr, nc))
#                    vis[nr][nc] = vis[r][c] + 1
#
#n = int(input())
#room = list(list(map(int, list(input().rstrip()))) for _ in range(n))
#vis = [[-1] * n for _ in range(n)]
#print(bfs())

# dijkstra
def dijkstra():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    heap = []
    heappush(heap, (0, 0, 0))
    vis[0][0] = True
    while heap:
        cnt, r, c = heappop(heap)
        if r == n-1 and c == n-1:
            return cnt
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if -1<nr<n and -1<nc<n and vis[nr][nc] == False:
                vis[nr][nc] = True
                if room[nr][nc]:
                    heappush(heap, (cnt, nr, nc))
                    vis[nr][nc] = vis[r][c]
                else:
                    heappush(heap, (cnt+1, nr, nc))

n = int(input())
room = list(list(map(int, list(input().rstrip()))) for _ in range(n))
vis = [[False] * n for _ in range(n)]
print(dijkstra())
