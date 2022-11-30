import sys
input = sys.stdin.readline

def dfs(li, i):
    stack = []
    stack.append(i)
    tmp = 0
    while stack:
        j = stack.pop()
        for k in li[j]:
            if not vis[k]:
                vis[k] = True
                stack.append(k)
                tmp += 1
    return tmp

n, m = map(int, input().split())
hvr = [[] for _ in range(n+1)]
ltr = [[] for _ in range(n+1)]
for _ in range(m):
    h, l = map(int, input().split())
    hvr[l].append(h)
    ltr[h].append(l)

cnt = 0
for i in range(1, n+1):
    vis = [False] * (n+1)
    if dfs(hvr, i) >= (n+1)//2:
        cnt += 1
    if dfs(ltr, i) >= (n+1)//2:
        cnt += 1
print(cnt)
