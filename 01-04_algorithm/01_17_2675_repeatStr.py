import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    r, s = map(str, input().split())
    for i in s:
        print(i*int(r), end='')
    print()
