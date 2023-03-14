import sys
input = sys.stdin.readline

def tsp(now, x, cost):
    global ans
    # escape
    if x == n:
        if w[now][0]:
            ans = min(ans, cost+w[now][0])
        return
    # recursion
    for next in range(1, n):
        if w[now][next] and not visited[next]:
            visited[next] = True
            tsp(next, x+1, cost+w[now][next])
            visited[next] = False

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
ans = 10**7

tsp(0, 1, 0)
print(ans)
