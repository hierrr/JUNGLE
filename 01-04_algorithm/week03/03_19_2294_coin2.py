import sys
from collections import deque
input = sys.stdin.readline

# dfs
def bfs():
    queue = deque()
    for c in coin:
        if c <= k:
            queue.append((c, 1))
            vis[c] = True
    while queue:
        val, cnt = queue.popleft()
        if val == k:
            return cnt
        for c in coin:
            if val+c <= k and not vis[val+c]:
                vis[val+c] = True
                queue.append((val+c, cnt+1))
    return -1

n, k = map(int, input().split())
coin = set(int(input()) for _ in range(n))
vis = [False] * (k+1)
print(bfs())

## dp
#n, k = map(int, input().split())
#coin = set(int(input()) for _ in range(n))
## min nums of coins
#dp = [10001 for _ in range(k+1)]
#dp[0] = 0
#for c in coin:
#    for i in range(c, k+1):
#        if i-c >= 0:
#            dp[i] = min(dp[i], dp[i-c]+1)
#print(-1 if dp[k] == 10001 else dp[k])
## count cases
#dp = [0 for _ in range(k+1)]
#dp[0] = 1
#for c in coin:
#    for i in range(c, k+1):
#        if i-c >= 0:
#            dp[i] += dp[i-c]
#print(dp[k])
