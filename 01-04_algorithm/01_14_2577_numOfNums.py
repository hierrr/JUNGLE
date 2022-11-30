import sys
input = sys.stdin.readline

n = 1
for i in range(3):
    n *= int(input())
s = str(n)

for j in range(0, 10):
    print(s.count(str(j)))
