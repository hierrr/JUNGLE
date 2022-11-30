import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

##1 pythonic, pivot = mid
#def quick_sort(li):
#    # escape
#    if len(li) <= 1:
#        return li
#
#    pivot = li[len(li)//2]
#    less = []
#    greater = []
#    equal = []
#
#    for i in li:
#        if i < pivot:
#            less.append(i)
#        elif i > pivot:
#            greater.append(i)
#        else:
#            equal.append(i)
#
#    return quick_sort(less) + equal + quick_sort(greater)

##2 pivot = start
#def quick_sort(li, start, end):
#    # escape
#    if start >= end:
#        return
#    
#    pivot = start
#    left, right = start+1, end
#
#    while left <= right:
#        # less than pivot
#        while left <= end and li[left] <= li[pivot]:
#            left += 1
#        # greater than pivot
#        while right > start and li[pivot] <= li[right]:
#            right -= 1
#
#        # if left/right crossed
#        if left > right:
#            li[right], li[pivot] = li[pivot], li[right]
#        else:
#            li[right], li[left] = li[left], li[right]
#
#    quick_sort(li, start, right-1)
#    quick_sort(li, right+1, end)

#3 partition and sort
def quick_sort(li, start, end):
    # sort and return next pivot_idx
    def partition(start, end):
        # pivot start from end
        pivot = (start+end)//2
        left, right = start, end
        
        while left < right:
            while left < right and li[left] < li[pivot]:
                left += 1
            while left < right and li[pivot] <= li[right]:
                right -= 1
            if left < right:
                if left == pivot:
                    pivot = right
                li[left], li[right] = li[right], li[left]
        li[pivot], li[right] = li[right], li[pivot]
        return right
    # sort recursively
    # if start/end crossed, escape
    if start < end:
        pivot = partition(start, end)
        quick_sort(li, start, pivot-1)
        quick_sort(li, pivot+1, end)
    return li

n = int(input())
li = [int(input()) for _ in range(n)]

##1
#sorted_li = quick_sort(li)
#print(*sorted_li, sep="\n")

#2 and #3
quick_sort(li, 0, n-1)
print(*li, sep="\n")
