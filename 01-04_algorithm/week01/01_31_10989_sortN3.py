import sys
input = sys.stdin.readline

n = int(input())
li = [0] * 10001

for _ in range(n):
    li[int(input())] += 1

for i in range(1, 10001):
    for _ in range(li[i]):
        print(i)

## enumerate
#for i, v in enumerate(li):
#    for _ in range(v):
#        print(i)
