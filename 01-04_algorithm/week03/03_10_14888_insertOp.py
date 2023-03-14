import sys
input = sys.stdin.readline

def dfs(dpt, cal, pls, mns, mul, div):
    global mx, mn
    # escape
    if dpt == n:
        mx = max(mx, cal)
        mn = min(mn, cal)
        return
    # plus
    if pls:
        dfs(dpt+1, cal+a[dpt], pls-1, mns, mul, div)
    # minus
    if mns:
        dfs(dpt+1, cal-a[dpt], pls, mns-1, mul, div)
    # multiply
    if mul:
        dfs(dpt+1, cal*a[dpt], pls, mns, mul-1, div)
    # divide
    if div:
        dfs(dpt+1, int(cal/a[dpt]), pls, mns, mul, div-1)

n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
mx, mn = -10**9, 10**9
dfs(1, a[0], *op)
print(mx, mn, sep="\n")
