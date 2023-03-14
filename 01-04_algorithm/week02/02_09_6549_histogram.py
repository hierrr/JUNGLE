import sys
input = sys.stdin.readline

## divide and conquer
#def dc(li, start, end):
#    # escape
#    if start == end:
#        return li[start]
#    # divide
#    mid = (start+end)//2
#    l = dc(li, start, mid)
#    r = dc(li, mid+1, end)
#    # conquer
#    pl, pr = mid, mid+1
#    h, w = min(li[pl], li[pr]), 2
#    a = h*w
#    while start <= pl and pr <= end:
#        hl = li[pl-1] if start < pl else 0
#        hr = li[pr+1] if pr < end else 0
#        h = min(h, max(hl, hr))
#        if hl > hr: pl -= 1
#        else: pr += 1
#        w += 1
#        a = max(a, h*w)
#    # return
#    return(max(a, l, r))
#    
#while True:
#    n, *h = map(int, input().split())
#    if n == 0:
#        break
#    print(dc(h, 0, n-1))

# stack
while True:
    n, *h = map(int, input().split())
    if not n:
        break
    # clear at last(n+1)
    h.append(0)
    stack = []
    a = 0
    for i in range(n+1):
        j = i
        while stack and stack[-1][1] >= h[i]:
            j, th = stack.pop()
            a = max(a, (i-j)*th)
        # not stack or h[j] <= h[i]
        stack.append((j, h[i]))
    print(a)
