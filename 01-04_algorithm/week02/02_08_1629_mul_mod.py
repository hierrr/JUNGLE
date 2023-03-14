import sys
input = sys.stdin.readline

def rec(n, p, d):
    if p == 1:
        return n%d
    tmp = rec(n, p//2, d)
    if p%2 == 0:
        return (tmp**2)%c
    else:
        return (a*tmp**2)%c

a, b, c = map(int, input().split())
print(rec(a, b, c))
