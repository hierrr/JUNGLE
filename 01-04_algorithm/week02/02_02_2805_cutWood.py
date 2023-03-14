import sys
input = sys.stdin.readline

def binary_search(li, start, end):
    while start <= end:
        mid = (start+end)//2
        tmp = 0
    
        for i in w:
            if i > mid:
                tmp += i - mid
    
        if tmp >= m:
            start = mid+1
        else:
            end = mid-1

    return end

n, m = map(int, input().split())
w = list(map(int, input().split()))

print(binary_search(w, 1, max(w)))
