import sys
input = sys.stdin.readline

def is_Prime(x):
    for i in range(2, int(x**.5)+1):
        if x%i == 0:
            return False
    return True

prime_li = []
for j in range(2, 10000):
    if is_Prime(j) == True:
        prime_li.append(j)

t = int(input())
for _ in range(t):
    n = int(input())
    for a in range(n//2, 1, -1):
        b = n-a
        if is_Prime(a) == 1 and is_Prime(b) == 1:
            print(a, b)
            break
