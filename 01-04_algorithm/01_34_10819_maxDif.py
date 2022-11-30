import sys
import itertools
input = sys.stdin.readline

# math
n = int(input())
li = sorted(list(map(int, input().split())))
mid = (n-1)//2
ans = 0
# even n
if not n%2:
    ans -= sum(li[:mid])*2 + li[mid]
    ans += li[mid+1] + sum(li[mid+1:])*2
# odd n
else:
    ans -= sum(li[:mid-1])*2 + li[mid-1]
    ans += li[mid+1] + sum(li[mid+1:])*2
    ans += max(abs(li[mid-1]-li[mid]), abs(li[mid]-li[mid+1]))
print(ans)

## math_short
#n=int(input())
#l=sorted(list(map(int,input().split())))
#m=(n-1)//2
#q=m-n%2
#w=m+n%2+(n-1)%2
#a=-sum(l[:q])*2-l[q]+l[w]+sum(l[w+1:])*2
#print(a+max(l[m]-l[m-1],l[m+1]-l[m]) if n%2 else a)

## permutation
#n = int(input())
#li = list(map(int, input().split()))
#
#perm_li = list(itertools.permutations(li, n))
#diff_li = []
#
#for i in range(len(perm_li)):
#    diff = 0
#    for j in range(n-1):
#        diff += abs(perm_li[i][j]-perm_li[i][j+1])
#    diff_li.append(diff)
#
#print(max(diff_li))
