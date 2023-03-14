import sys
input = sys.stdin.readline

n, k = map(int, input().split())
item = list(list(map(int, input().split())) for _ in range(n))
npsk = [0] * (k+1)

for w, v in item:
    for i in range(k, w-1, -1):
        npsk[i] = max(npsk[i], npsk[i-w] + v)
print(npsk[k])
