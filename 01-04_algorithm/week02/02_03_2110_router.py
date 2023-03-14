import sys
input = sys.stdin.readline

def binary_search(li, start, end):
    ans = 1

    while start <= end:
        mid = (start+end)//2
        tmp = li[0]
        cnt = 1
    
        for cur in li:
            if cur - tmp >= mid:
                cnt += 1
                tmp = cur
    
        if cnt >= c:
            start = mid+1
            ans = mid
        else:
            end = mid-1

    return ans

n, c = map(int, input().split())
li = sorted([int(input()) for _ in range(n)])
ans = 1

print(binary_search(li, 1, li[-1]-li[0]))
