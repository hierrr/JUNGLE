import sys
input = sys.stdin.readline

class min_heap():
    def __init__(self):
        self.heap = []
        self.num = 0
    def push(self, x):
        self.heap.append(x)
        self.num += 1
        idx = len(self.heap)-1
        while 0 <= idx:
            p_idx = self.parent(idx)
            if 0 <= p_idx and self.heap[p_idx] > self.heap[idx]:
                self.swap(idx, p_idx)
                idx = p_idx
            else:
                break
    def pop(self):
        idx = len(self.heap)-1
        if idx < 0:
            return -1
        self.swap(0, idx)
        min_v = self.heap.pop()
        self.num -= 1
        self.min_heapify(0)
        return min_v
    def min_heapify(self, i):
        l_idx = self.left_child(i)
        r_idx = self.right_child(i)
        idx = i
        # heap[idx] = min(heap[idx], heap[l_idx], heap[r_idx])
        if l_idx <= self.num-1 and self.heap[idx] > self.heap[l_idx]:
            idx = l_idx
        if r_idx <= self.num-1 and self.heap[idx] > self.heap[r_idx]:
            idx = r_idx
        if idx != i:
            self.swap(i, idx)
            self.min_heapify(idx)
    def left_child(self, idx):
        return idx*2+1
    def right_child(self, idx):
        return idx*2+2
    def parent(self, idx):
        return (idx-1)//2
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
    def size(self):
        return self.num
    def peek(self):
        return self.heap[0]
    def show(self):
        return self.heap

min_heap = min_heap()
func = {
    "pop" : lambda heap: heap.pop(),
    "size" : lambda heap: heap.size(),
    "peek" : lambda heap: heap.peek(),
    "show" : lambda heap: heap.size()
}

while True:
    cmd = input().split()
    fn = cmd[0]
    if not fn:
        break
    elif fn == "push":
        min_heap.push(int(cmd[1]))
    else:
        print(func[fn](min_heap))
    print(min_heap.show())
