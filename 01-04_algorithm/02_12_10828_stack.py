import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    cmd = input().split()
    fn = cmd[0]

    if fn == "push":
        stack.append(int(cmd[1]))

    elif fn == "pop":
        print(stack.pop() if stack else -1)

    elif fn == "size":
        print(len(stack))

    elif fn == "empty":
        print(0 if stack else 1)

    elif fn == "top":
        print(stack[-1] if stack else -1)
