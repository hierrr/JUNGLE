import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

def is_Prime(x):
    for i in range(2, int(x**.5)+1):
        if x%i == 0:
            return False
    return True

cnt = 0
for i in li:
    if i != 1:
        if is_Prime(i) == True:
            cnt += 1
print(cnt)
