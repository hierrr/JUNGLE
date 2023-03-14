import sys
input = sys.stdin.readline

# bisect
def lower_bound(data, target, start=0, end=None):
    if end is None:
        end = len(data)
    while start < end:
        mid = (start+end)//2
        if data[mid] < target:
            start = mid+1
        else:
            end = mid
    return start

n = int(input())
li = sorted(list(map(int, input().split())))

l, r = 0, n-1
dif = 10**10
for i in range(n):
    j = lower_bound(li, -li[i], i+1, n-1)
    if i < j-1 < n and abs(li[i] + li[j-1]) < dif:
        dif = abs(li[i] + li[j-1])
        l, r = i, j-1
    if i < j < n and abs(li[i] + li[j]) < dif:
        dif = abs(li[i] + li[j])
        l, r = i, j
print(li[l], li[r])

## two pointer
#n = int(input())
#li = sorted(list(map(int, input().split())))
#
#s, e = 0, n-1
#dif = 10**10
#l, r = 0, n-1
#
#while s < e:
#    tmp = li[s] + li[e]
#    if abs(dif) > abs(tmp):
#        dif = tmp
#        l, r = s, e
#    if tmp > 0:
#        e -= 1
#    else:
#        s += 1
#
#print(li[l], li[r])

## sort abs
#n = int(input())
#s = list(map(int, input().split()))
#s.sort(key=lambda x: abs(x))
#
#dif = 10**10
#idx = 0
#
#for i in range(0, n-1):
#    tmp = s[i] + s[i+1]
#    if abs(dif) > abs(tmp):
#        dif = tmp
#        idx = i
#
#if s[idx] < s[idx+1]:
#    print(s[idx], s[idx+1])
#else:
#    print(s[idx+1], s[idx])
