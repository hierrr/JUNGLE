import sys
input = sys.stdin.readline

def lower_bound(data, target, start, end):
    ret = 0
    while start <= end:
        mid = (start+end)//2
        if data[mid] < target:
            start = mid+1
        else:
            ret = mid
            end = mid-1
    return ret

m, n, l = map(int, input().split())
mx = sorted(list(map(int, input().split())))
a_li = sorted(list(list(map(int, input().split()))) for _ in range(n))

cnt = 0
for ax,ay in a_li:
    i = lower_bound(mx, ax, 0, m-1)
    if abs(mx[i-1]-ax)+ay <= l or abs(mx[i]-ax)+ay <= l:
        cnt += 1

print(cnt)
