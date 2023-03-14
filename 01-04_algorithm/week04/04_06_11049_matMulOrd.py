import sys
input = sys.stdin.readline

# pypy
n = int(input())
mat = list(list(map(int, input().split())) for _ in range(n))
dp = [[0] * n for _ in range(n)]

for d in range(1, n):
    for i in range(n-d):
        j = i + d
        dp[i][j] = 2**32
        for k in range(i, j):
            dp[i][j] = min(dp[i][j],
            # mul(1:n) = mul(1:k) + mul(k+1:n) + mul(k, k+1)
            dp[i][k] + dp[k+1][j] +mat[i][0]*mat[k][1]*mat[j][1])
print(dp[0][n-1])

## python3
#n = int(input())
#mat = list(list(map(int, input().split())) for _ in range(n))
#mat = [x for x, _ in mat] + [mat[-1][1]]
#dp = [[0] * n for _ in range(n)]
#
#for d in range(1, n):
#    for i in range(n-d):
#        j = i + d
#        ij = mat[i] * mat[j+1]
#        tmp = min(ik + ij*k + kj for ik, k, kj in zip(dp[i][i:j], mat[i+1:j+1] ,dp[j][i+1:j+1]))
#        dp[i][j] = dp[j][i] = tmp
#print(dp[0][n-1])
