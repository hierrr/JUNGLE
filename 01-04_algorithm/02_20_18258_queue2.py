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

    def pop(self):
        if not self.num:
            print(-1)
            return
        tmp = self.pf
        print(tmp.data)
        if tmp.next:
            self.pf = tmp.next
            self.pf.prev = None
        else:
            self.pf = None
            self.pb = None
        self.num -= 1

    def size(self):
        print(self.num)

    def empty(self):
        print(1 if not self.num else 0)

    def front(self):
        if not self.num:
            print(-1)
            return
        print(self.pf.data)

    def back(self):
        if not self.num:
            print(-1)
            return
        print(self.pb.data)

n = int(input())
queue = deque()
func = {
    "pop" : lambda queue: queue.pop(),
    "size" : lambda queue : queue.size(),
    "empty" : lambda queue : queue.empty(),
    "front" : lambda queue : queue.front(),
    "back" : lambda queue : queue.back()
}

for _ in range(n):
    cmd = input().split()
    fn = cmd[0]
    if fn == "push":
        queue.push(int(cmd[1]))
    else:
        func[fn](queue)
