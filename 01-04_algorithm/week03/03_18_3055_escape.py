import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    for i in range(r):
        for j in range(c):
            if mat[i][j] == "*":
                queue.appendleft((i, j))
                vis[i][j] = 0
            elif mat[i][j] == "S":
                queue.append((i, j))
                vis[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1<nx<r and -1<ny<c and vis[nx][ny] == -1:
                if mat[nx][ny] == "*" or mat[nx][ny] == "X":
                    continue
                if mat[nx][ny] == "D" and mat[x][y] == "*":
                    continue
                if mat[nx][ny] == "D" and mat[x][y] == "S":
                    return vis[x][y] + 1
                queue.append((nx, ny))
                vis[nx][ny] = vis[x][y] + 1
                mat[nx][ny] = mat[x][y]
    return "KAKTUS"

r, c = map(int, input().split())
mat = list(list(input().rstrip()) for _ in range(r))
vis = [[-1] * c for _ in range(r)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
print(bfs())
