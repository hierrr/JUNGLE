import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stack = []
    vps = True
    case = input().rstrip()
    for c in case:
        if c == ")":
            if not stack:
                vps = False
                break
            else:
                stack.pop()
        else:
            stack.append(c)
    if vps and not stack:
        print("YES")
    else:
        print("NO")
