import sys
input = sys.stdin.readline

# dp and bisect
def lower_bound(data, target, start, end):
    while start < end:
        mid = (start+end)//2
        if data[mid] < target:
            start = mid+1
        else:
            end = mid
    return start

n = int(input())
a = list(map(int, input().split()))

dp = [a[0]]
cnt = 1

for x in a:
    if x > dp[cnt-1]:
        dp.append(x)
        cnt += 1
    else:
        i = lower_bound(dp, x, 0, cnt-1)
        dp[i] = x

print(cnt)
