import sys
input = sys.stdin.readline

# dp
n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
## get lis
#mdp = max(dp)
#idx = dp.index(mdp)
#lis = []
#while idx >= 0:
#    if dp[idx] == mdp:
#        lis.append(a[idx])
#        mdp -= 1
#    idx -= 1
#lis.reverse()
#print(*lis)
