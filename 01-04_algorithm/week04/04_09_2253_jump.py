import sys
inf = sys.maxsize
input = sys.stdin.readline

n, m = map(int, input().split())
stn = set(list(int(input()) for _ in range(m)))
# sum(arithm seq, a0=1, d=1) = k(k+1)/2 = n
# k = (2n-k)**.5 >> (2*n)**.5
dp = [[inf] * (int((2*n)**.5)+2) for _ in range(n+1)]

dp[1][0] = 0
for i in range(2, n+1):
    if i in stn:
        continue
    for j in range(1, int((2*i)**.5)+1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1
cnt = min(dp[n])
print(cnt if cnt != inf else -1)
