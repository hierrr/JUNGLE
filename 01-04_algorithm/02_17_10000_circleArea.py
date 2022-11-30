import sys
input = sys.stdin.readline

n = int(input())
c = []
for _ in range(n):
    x, r = map(int, input().split())
    # l or r, coord, status(tangent: True)
    c.append(["(", x-r, False])
    c.append([")", x+r, False])
c.sort(key=lambda x: (x[1], -ord(x[0])))

stack = []
cnt = 1

for i in range(n*2):
    # open circle
    if c[i][0] == "(":
        if stack:
            # (( or )(, status = True
            if stack[-1][1] == c[i][1] or stack[-1][1] == c[i][1]:
                stack[-1][2] = True
            else:
                stack[-1][2] = False
        stack.append(c[i])
    # close circle
    else:
        tmp = stack.pop()
        # (.coord = ).coord
        if stack and stack[-1][2]:
            stack[-1][1] = c[i][1]
        # ))
        if tmp[2] and tmp[1] == c[i][1]:
            cnt += 1
        cnt += 1

print(cnt)
