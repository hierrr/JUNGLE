import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = input().rstrip()

stack = []
for i in a:
    if not stack or stack[-1] >= i or not k:
        stack.append(i)
    else:
        while stack and k:
            if stack[-1] < i:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(i)
while k:
    tmp = stack.pop()
    if stack[-1] < tmp:
        stack[-1] = tmp
    k -= 1
print(''.join(stack))
