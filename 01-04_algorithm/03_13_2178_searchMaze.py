import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    queue = deque()
    queue.append((0, 0))
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if -1<nr<n and -1<nc<m:
                if maze[nr][nc] == 1:
                    maze[nr][nc] = maze[r][c] + 1
                    queue.append((nr, nc))
    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = list(list(map(int, list(input().rstrip()))) for _ in range(n))
print(bfs())
