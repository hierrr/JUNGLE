import sys
inf = sys.maxsize
input = sys.stdin.readline

def tsp(now, vis):
    # visited all
    if vis == (1<<n) - 1:
        return w[now][0] if w[now][0] else inf
    # memoization
    if dp[now][vis]:
        return dp[now][vis]

    cost = inf
    for i in range(1, n):
        # not visited and visitable
        if not (vis>>i)%2 and w[now][i]:
            tmp = tsp(i, vis|(1<<i))
            cost = min(cost, tmp + w[now][i])
    dp[now][vis] = cost
    return cost

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(1<<n) for _ in range(n)]
print(tsp(0, 1))

## dist
#def tsp(now, vis):
#    # visited all
#    if vis == (1<<n) - 1:
#        return dis[now][0] if dis[now][0] else inf
#    # memoization
#    if dp[now][vis]:
#        return dp[now][vis]
#
#    cost = inf
#    for i in range(1, n):
#        # not visited and visitable
#        if not (vis>>i)%2 and dis[now][i]:
#            tmp = tsp(i, vis|(1<<i))
#            cost = min(cost, tmp + dis[now][i])
#    dp[now][vis] = cost
#    return cost
#
#n = int(input())
#mat = list(list(map(int, input().split())) for _ in range(n))
#dis = [[0] * n for _ in range(n)]
#for i in range(n):
#    for j in range(i, n):
#        dis[i][j] = dis[j][i] = ((mat[i][0] - mat[j][0])**2 + (mat[i][1] - mat[j][1])**2)**.5
#dp = [[0]*(1<<n) for _ in range(n)]
#print(tsp(0, 1))
