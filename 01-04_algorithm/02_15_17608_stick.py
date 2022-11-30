import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    h = int(input())

    if not stack or stack[-1] > h:
        stack.append(h)
    else:
        for i in range(len(stack)-1, -1, -1):
            if stack[i] <= h:
                stack.pop()
            else:
                break
        stack.append(h)

print(len(stack))
