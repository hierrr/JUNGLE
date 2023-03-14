import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    li = list(map(int, input().split()))
    avr = sum(li[1:])/li[0]
    cnt = 0
    for i in li[1:]:
        if i > avr:
            cnt += 1
    print(f"{(cnt*100/li[0]):.3f}%")
