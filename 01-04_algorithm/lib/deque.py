import sys
input = sys.stdin.readline

class node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class deque():
    def __init__(self):
        self.pf = None
        self.pb = None
        self.num = 0
    def push(self, x):
        tmp = node(x)
        if not self.pf:
            self.pf = tmp
            self.pb = tmp
        else:
            tmp.prev = self.pb
            self.pb.next = tmp
            self.pb = tmp
        self.num += 1
    def push_front(self, x):
        tmp = node(x)
        if not self.pf:
            self.pf = tmp
            self.pb = tmp
        else:
            tmp.next = self.pf
            self.pf.prev = tmp
            self.pf = tmp
        self.num += 1
    def pop(self):
        if not self.num:
            return -1
        tmp = self.pf
        if tmp.next:
            self.pf = tmp.next
            self.pf.prev = None
        else:
            self.pf = None
            self.pb = None
        self.num -= 1
        return tmp.data
    def pop_back(self):
        if not self.num:
            return -1
        tmp = self.pb
        if tmp.prev:
            self.pb = tmp.prev
            self.pb.next = None
        else:
            self.pf = None
            self.pb = None
        self.num -= 1
        return tmp.data
    def size(self):
        return self.num
    def empty(self):
        return 1 if not self.num else 0
    def front(self):
        if not self.num:
            return -1
        return self.pf.data
    def back(self):
        if not self.num:
            return -1
        return self.pb.data
    def rotate(self, r):
        if not self.num:
            return -1
        if r <= 0:
            for _ in range(-r):
                self.push(self.pop())
        else:
            for _ in range(self.num - r):
                self.push(self.pop())
    def show(self):
        tab = []
        cur = self.pf
        while cur:
            tab.append(cur.data)
            cur = cur.next
        return tab

deque = deque()
func = {
    "pop" : lambda deque: deque.pop(),
    "pop_back" : lambda deque: deque.pop_back(),
    "size" : lambda deque : deque.size(),
    "empty" : lambda deque : deque.empty(),
    "front" : lambda deque : deque.front(),
    "back" : lambda deque : deque.back(),
    "show" : lambda deque : deque.show()
}
while True:
    cmd = input().split()
    fn = cmd[0]
    if not fn:
        break
    elif fn == "push":
        deque.push(int(cmd[1]))
    elif fn == "push_front":
        deque.push_front(int(cmd[1]))
    elif fn == "rotate":
        deque.rotate(int(cmd[1]))
    else:
        print(func[fn](deque))
    print(deque.show())
