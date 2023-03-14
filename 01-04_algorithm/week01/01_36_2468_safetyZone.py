import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(h, r, c):
    vi[r][c] = True

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if -1 < nr < n and -1 < nc < n:
            if vi[nr][nc] or li[nr][nc] <= h:
                continue
            dfs(h, nr, nc)
    return

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

h_set = set()
for l in li:
    h_set.update(l)

ans = {1}
# ans = 1

for h in h_set:
# for h in range(101):
    vi = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if vi[i][j] or li[i][j] <= h:
                continue
            cnt += 1
            dfs(h, i, j)
    ans.add(cnt)
    # ans = max(ans, cnt)

print(max(ans))
# print(ans)
