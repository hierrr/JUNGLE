import sys
input = sys.stdin.readline
# tree[node] = sum(a[start:end+1]) = left_child + right_child
def init(node=1, start=0, end=None):
    if end is None:
        end = len(a)-1
    if start == end:
        tree[node] = a[start]
        return
    mid = (start+end)//2
    init(node*2, start, mid)
    init(node*2+1, mid+1, end)
    tree[node] = tree[node*2] + tree[node*2+1]
# change leaf val and its parents
def update(node, idx, val, start=0, end=None):
    if end is None:
        end = len(a)-1
    if not (start <= idx <= end):
        return
    if start == end:
#        a[node] = val
        tree[node] = val
        return
    mid = (start+end)//2
    update(node*2, idx, val, start, mid)
    update(node*2+1, idx, val, mid+1, end)
    tree[node] = tree[node*2] + tree[node*2+1]
# update in range left to right
def update_lazy(node, start, end):
    if lazy[node]:
        tree[node] += (end-start+1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0
def update_range(node, dif, left, right, start=0, end=None):
    if end is None:
        end = len(a)-1
    update_lazy(node, start, end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] += (end-start+1) * dif
        if start != end:
            lazy[node*2] += dif
            lazy[node*2+1] += dif
        return
    mid = (start+end)//2
    update_range(node*2, dif, left, right, start, mid)
    update_range(node*2+1, dif, left, right, mid+1, end)
    tree[node] = tree[node*2] + tree[node*2+1]
# node for range left to right, in tree start to end
def query(node, left, right, start=0, end=None):
    if end is None:
        end = len(a)-1
    # if need to update lazy
    if lazy:
        update_lazy(node, start, end)
    # out of range
    if left > end or right < start:
        return 0
    # [start:end+1] in [left:right+1]
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    suml = query(node*2, left, right, start, mid)
    sumr = query(node*2+1, left, right, mid+1, end)
    return suml + sumr

a = list(map(int, input().split()))
tree = [0 for _ in range(len(a)*4)]
lazy = [0 for _ in range(len(a)*4)]
init()
print(tree)
while True:
    f, *q = map(int, input().split())
    if not f:
        break
    # update
    elif f == 1:
        i, v = q
        print(tree)
        update(1, i-1, v)
        print(tree)
    # update in range
    elif f == 2:
        l, r, d = q
        print(tree)
        update_range(1, d, l-1, r-1)
        print(tree)
    # query
    else:
        l, r = q
        print(query(1, l-1, r-1))
