import sys
input = sys.stdin.readline

s = input().rstrip()
stack = []
val = 0

for c in s:
    # ( = 2, [ = 3, inner val
    if c == "(":
        stack.append([c, 2, 0])
    elif c == "[":
        stack.append([c, 3, 0])
    else:
        if not stack:
            val = 0
            break
        else:
            t = stack.pop()
            # [) or (]
            if (c == ")" and t[0] == "[") or (c == "]" and t[0] == "("):
                val = 0
                break
            else:
                if not t[2]:
                    t[2] = 1
                tmp = t[1] * t[2]
                if not stack:
                    val += tmp
                else:
                    stack[-1][2] += tmp
print(val)
