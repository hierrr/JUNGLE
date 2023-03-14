import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

## dfs(stack)
#def dfs(r, c, vis):
#    stack = []
#    stack.append((r, c))
#    while stack:
#        cr, cc = stack.pop()
#        if not vis[cr][cc]:
#            vis[cr][cc] = True
#            sea = 0
#            # check num of adj sea
#            for i in range(4):
#                nr = cr + dr[i]
#                nc = cc + dc[i]
#                if not vis[nr][nc]:
#                    if not mat[nr][nc]:
#                        sea += 1
#                    else:
#                        stack.append((nr, nc))
#            mat[cr][cc] = max(mat[cr][cc]-sea, 0)
#            if not mat[cr][cc]:
#                icbg[(cr, cc)] = False

# dfs(rec)
def dfs(r, c, vis):
    vis[r][c] = True
    sea = 0
    # check num of adj sea
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not vis[nr][nc]:
            if not mat[nr][nc]:
                sea += 1
            else:
                dfs(nr, nc, vis)
    mat[r][c] = max(mat[r][c]-sea, 0)
    if not mat[r][c]:
        icbg[(r, c)] = False

def chk(yr):
    while sum(icbg.values()):
        vis = [[False] * m for _ in range(n)]
        cnt = 1
        # check ice pos only
        for (r, c), ice in icbg.items():
            if ice and not vis[r][c]:
                if cnt >= 2:
                    return yr
                dfs(r, c, vis)
                cnt += 1
        yr += 1
    return 0

n, m = map(int, input().split())
mat = list(list(map(int, input().split())) for _ in range(n))
# memo ice pos
icbg = dict()
for i in range(1, n-1):
    for j in range(1, m-1):
        if mat[i][j]:
            icbg[(i, j)] = True
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
print(chk(0))
