import sys
input = sys.stdin.readline

class bitset():
    def __init__(self):
        self.set = 0
    def add(self, x):
        self.set |= (1<<x)
    def remove(self, x):
        self.set &= ~(1<<x)
    def check(self, x):
        return 1 if (self.set & (1<<x)) else 0
    def toggle(self, x):
        self.set ^= (1<<x)
    def all(self):
        self.set = (1<<21) - 1
    def empty(self):
        self.set = 0
    def show(self):
        return bin(self.set)

s = bitset()
func = {
    "all" : lambda s: s.all(),
    "empty" : lambda s: s.empty(),
    "show" : lambda s: s.show()
}
while True:
    cmd = input().split()
    fn = cmd[0]
    if not fn:
        break
    elif fn == "add":
        s.add(int(cmd[1]))
    elif fn == "remove":
        s.remove(int(cmd[1]))
    elif fn == "check":
        print(s.check(int(cmd[1])))
    elif fn == "toggle":
        s.toggle(int(cmd[1]))
    else:
        func[fn](s)
    print(s.show())
