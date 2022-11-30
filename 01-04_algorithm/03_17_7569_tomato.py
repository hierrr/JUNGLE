import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1 and not vis[i][j][k]:
                    queue.append((i, j, k))
                    vis[i][j][k] = True
    while queue:
        z, r, c = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if -1<nz<h and -1<nr<n and -1<nc<m:
                if not box[nz][nr][nc] and not vis[nz][nr][nc]:
                    queue.append((nz, nr, nc))
                    box[nz][nr][nc] = box[z][r][c] + 1
                    vis[nz][nr][nc] = True

def chk():
    cnt = 0
    for i in box:
        for j in i:
            for k in j:
                if not k:
                    return -1
            cnt = max(cnt, max(j))
    return cnt-1

m, n, h = map(int, input().split())
box = list(list(list(map(int, input().split())) for _ in range(n)) for _ in range(h))
vis = [[[False] * m for _ in range(n)] for _ in range(h)]
dz = [0, 0, 0, 0, 1, -1]
dr = [0, 1, 0, -1, 0, 0]
dc = [1, 0, -1, 0, 0, 0]
bfs()
print(chk())
