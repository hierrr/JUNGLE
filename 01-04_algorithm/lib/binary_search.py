import bisect

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

def upper_bound(data, target, start=0, end=None):
    if end is None:
        end = len(data)
    while start < end:
        mid = (start+end)//2
        if data[mid] <= target:
            start = mid+1
        else:
            end = mid
    return start

a = [1, 3, 5, 7, 9]

print("lb/ub(a, 3, 0, 4)")
print(lower_bound(a, 3, 0, 4))
print(upper_bound(a, 3, 0, 4))
print("bl/br(a, 3, 0, 4)")
print(bisect.bisect_left(a, 3, 0, 4))
print(bisect.bisect_right(a, 3, 0, 4))

print("lb/ub(a, 4, 0, 4)")
print(lower_bound(a, 4, 0, 4))
print(upper_bound(a, 4, 0, 4))
print("bl/br(a, 4, 0, 4)")
print(bisect.bisect_left(a, 4, 0, 4))
print(bisect.bisect_right(a, 4, 0, 4))
