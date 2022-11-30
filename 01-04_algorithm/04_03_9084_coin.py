import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    k = int(input())
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    for c in coin:
        for i in range(c, k+1):
            if i-c >= 0:
                dp[i] += dp[i-c]
    print(dp[k])
