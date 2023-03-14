import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = list(int(input()) for _ in range(n))
coin.sort(reverse=True)

cnt = 0
for c in coin:
    cnt += k//c
    k %= c
print(cnt)
