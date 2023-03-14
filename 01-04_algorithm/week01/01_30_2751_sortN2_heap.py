import sys
import heapq
input = sys.stdin.readline

## pythonic
#def heap_sort(li):
#    heap = []
#    tab = []
#    # heap << value in li
#    for value in li:
#        heapq.heappush(heap, value)
#    # root in heap >> tab
#    for _ in range(len(heap)):
#        tab.append(heapq.heappop(heap))
#    return tab

def heap_sort(li):
    # set heap
    def heapify(li, i, size):
        # left, right child
        l, r = i*2+1, i*2+2
        # selected node
        s = i
        # s = max(li[s], li[l], li[r])
        if l <= size and li[s] < li[l]:
            s = l
        if r <= size and li[s] < li[r]:
            s = r
        # switch i and s
        if s != i:
            li[i], li[s] = li[s], li[i]
            return heapify(li, s, size)
    
    size = len(li)-1
    # set heap
    for i in range(size//2, -1, -1):
        heapify(li, i, size)
    # root >> li[-1] and heapify li[:-1]
    for i in range(size, 0, -1):
        li[i], li[0] = li[0], li[i]
        heapify(li, 0, i-1)

n = int(input())
li = [int(input()) for _ in range(n)]

heap_sort(li)
print(*li, sep="\n")
