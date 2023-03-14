import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    emp = list(list(map(int, input().split())) for _ in range(n))
    
    emp.sort(key=lambda x: x[0])  
    cnt = 1
    std = emp[0][1]
    for i in range(1, n):
        if emp[i][1] < std:
            std = emp[i][1]
            cnt += 1
    print(cnt)
