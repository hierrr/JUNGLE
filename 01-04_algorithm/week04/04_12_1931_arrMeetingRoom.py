import sys
input = sys.stdin.readline

n = int(input())
m = list(list(map(int, input().split())) for _ in range(n))
m.sort(key=lambda x: [x[1], x[0]])

cnt, tmp = 0, 0
for i in m:
    if i[0] >= tmp:
        tmp = i[1]
        cnt += 1
print(cnt)
