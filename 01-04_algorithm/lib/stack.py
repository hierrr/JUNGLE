import sys
input = sys.stdin.readline

## linked list
#class node():
#    def __init__(self, data):
#        self.data = data
#        self.blw = None
#        self.num = 0
#
#class stack():
#    def __init__(self):
#        self.pt = None
#        self.num = 0
#    def push(self, x):
#        tmp = node(x)
#        if self.pt:
#            tmp.blw = self.pt
#        self.pt = tmp
#        self.num += 1
#    def pop(self):
#        if not self.num:
#            return -1
#        tmp = self.pt.data
#        self.pt = self.pt.blw
#        self.num -= 1
#        return tmp
#    def size(self):
#        return self.num
#    def empty(self):
#        return 1 if not self.num else 0
#    def top(self):
#        if not self.num:
#            return -1
#        return self.pt.data
#    def show(self):
#        tab = []
#        cur = self.pt
#        while cur:
#            tab.append(cur.data)
#            cur = cur.blw
#        return tab[::-1]
#
#stack = stack()
#func = {
#    "pop" : lambda stack: stack.pop(),
#    "size" : lambda stack: stack.size(),
#    "empty" : lambda stack: stack.empty(),
#    "top" : lambda stack: stack.top()
#}
#while True:
#    cmd = input().split()
#    fn = cmd[0]
#    if not fn:
#        break
#    elif fn == "push":
#        stack.push(int(cmd[1]))
#    else:
#        print(func[fn](stack))
#    print(stack.show())

# array
class stack():
    def __init__(self):
        self.stk = []
        self.pt = -1
    def push(self, x):
        self.stk.append(x)
        self.pt += 1
    def pop(self):
        if self.pt == -1:
            return -1
        tmp = self.stk[self.pt]
        del self.stk[self.pt]
        self.pt -= 1
        return tmp
    def size(self):
        return self.pt + 1
    def empty(self):
        return 1 if self.pt == -1 else 0
    def top(self):
        if self.pt == -1:
            return -1
        return self.stk[self.pt]
    def show(self):
        return self.stk

stack = stack()
func = {
    "pop" : lambda stack: stack.pop(),
    "size" : lambda stack: stack.size(),
    "empty" : lambda stack: stack.empty(),
    "top" : lambda stack: stack.top()
}
while True:
    cmd = input().split()
    fn = cmd[0]
    if not fn:
        break
    elif fn == "push":
        stack.push(int(cmd[1]))
    else:
        print(func[fn](stack))
    print(stack.show())
