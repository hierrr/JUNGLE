import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# dfs(recursive)
def dfs(ex):
    tmp = 0
    for x in graph[ex]:
        if a[x]:
            tmp += 1
        else:
            if not vis[x]:
                vis[x] = True
                tmp += dfs(x)
    return tmp

def cnt():
    cnt = 0
    for i in range(1, n+1):
        # indoor
        if a[i]:
            for j in graph[i]:
                if a[j]:
                    cnt += 1
        # outdoor
        else:
            if not vis[i]:
                vis[i] = True
                tmp = dfs(i)
                cnt += tmp * (tmp-1)
    return cnt

n = int(input())
a = list(map(int, list("0" + input().rstrip())))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
vis = [False] * (n+1)
print(cnt())

## dfs(stack)
#n = int(input())
#a = list(map(int, list("0" + input().rstrip())))
#graph = [[] for _ in range(n+1)]
#for _ in range(n-1):
#    u, v = map(int, input().split())
#    graph[u].append(v)
#    graph[v].append(u)
#vis = [False] * (n+1)
#
#cnt = 0
#for i in range(1, n+1):
#    # indoor
#    if a[i]:
#        for j in graph[i]:
#            if a[j]:
#                cnt += 1
#    # outdoor
#    else:
#        if not vis[i]:
#            vis[i] = True
#            stack = []
#            tmp = 0
#            stack.append(i)
#            while stack:
#                j = stack.pop()
#                for k in graph[j]:
#                    if a[k]:
#                        tmp += 1
#                    else:
#                        if not vis[k]:
#                            vis[k] = True
#                            stack.append(k)
#            cnt += tmp * (tmp-1)
#print(cnt)
