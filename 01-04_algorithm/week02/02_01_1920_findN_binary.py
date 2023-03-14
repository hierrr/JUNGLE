import sys
input = sys.stdin.readline

# binary_search_iter
def binary_search(target, data, start, end):
    # data must be sorted
    while start <= end:
        mid = (start+end)//2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    print(1 if binary_search(i, a, 0, n-1) > -1 else 0)

## binary_search_rec
#def binary_search(target, start, end, data):
#    # data must be sorted
#    if start > end:
#        return -1 
#    mid = (start+end)//2
#
#    if data[mid] == target:
#        return mid
#    elif data[mid] < target:
#        start = mid + 1
#    else:
#        end = mid -1
#
#    return binary_search(target, start, end, data)
#
#n = int(input())
#a = sorted(list(map(int, input().split())))
#m = int(input())
#x = list(map(int, input().split()))
#
#for i in x:
#    print(1 if binary_search(i, 0, n-1, a) > -1 else 0)
