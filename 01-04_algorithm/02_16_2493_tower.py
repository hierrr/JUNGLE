import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

stack = []
ans = []

for i in range(n):
    for j in range(len(stack)-1, -1, -1):
        if not stack or stack[j][0] > h[i]:
            break
        else:
            stack.pop()
    ans.append(0 if not stack else stack[-1][1])
    stack.append((h[i], i+1))

print(*ans)
