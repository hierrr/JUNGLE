import sys
input = sys.stdin.readline

def isAP(n):
    if n >= 100:
        li = list(str(n))
        d0 = int(li[0]) - int(li[1])
        for i in range(1, len(li)-1):
            d = int(li[i]) - int(li[i+1])
            if d0 != d:
                return False
    return True

n = int(input())
cnt = 0
for i in range (1, n+1):
    if isAP(i) == True:
        cnt += 1
print(cnt)
