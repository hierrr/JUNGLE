import sys
input = sys.stdin.readline

class node():
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
class binary_search_tree():
    def __init__(self):
        self.root = None
    def search(self, key):
        pn = self.root
        while True:
            if not pn:
                return None
            if key == pn.key:
                return pn.data
            elif key < pn.key:
                pn = pn.left
            else:
                pn = pn.right
    def insert(self, key, data):
        def _insert(pn, key, data):
            if key == pn.key:
                return False
            if key < pn.key:
                if not pn.left:
                    pn.left = node(key, data)
                else:
                    _insert(pn.left, key, data)
            else:
                if not pn.right:
                    pn.right = node(key, data)
                else:
                    _insert(pn.right, key, data)
            return True
        if not self.root:
            self.root = node(key, data)
            return True
        else:
            return _insert(self.root, key, data)
    def remove(self, key):
        pn = self.root
        parent = None
        is_left = True
        while True:
            if not pn:
                return False
            if key == pn.key:
                break
            else:
                parent = pn
                if key < pn.key:
                    is_left = True
                    pn = pn.left
                else:
                    is_left = False
                    pn = pn.right
        if not pn.left:
            if pn == self.root:
                self.root = pn.right
            elif is_left:
                parent.left = pn.right
            else:
                parent.right = pn.right
        elif not pn.right:
            if pn == self.root:
                self.root = pn.left
            elif is_left:
                parent.left = pn.left
            else:
                parent.right = pn.left
        else:
            parent = pn
            left_child = pn.left
            is_left = True
            while left_child.right:
                parent = left_child
                left_child = left_child.right
                is_left = False
            pn.key = left_child.key
            pn.data = left_child.data
            if is_left:
                parent.left = left_child.left
            else:
                parent.right = left_child.left
        return True
    def show(self, reverse=False):
        self.ret = []
        def _show(pn):
            if not pn:
                return
            _show(pn.left)
            self.ret.append((pn.key, pn.data))
            _show(pn.right)
        def _show_rev(pn):
            if not pn:
                return
            _show_rev(pn.right)
            self.ret.append((pn.key, pn.data))
            _show_rev(pn.left)
        _show(self.root) if not reverse else _show_rev(self.root)
        return self.ret
    def min(self):
        if not self.root:
            return None
        pn = self.root
        while pn.left:
            pn = pn.left
        return pn.key
    def max(self):
        if not self.root:
            return None
        pn = self.root
        while pn.right:
            pn = pn.right
        return pn.key

bst = binary_search_tree()
func = {
    "show" : lambda bst: bst.show(),
    "showrev" : lambda bst: bst.show(reverse=True),
    "min" : lambda bst: bst.min(),
    "mindata" : lambda bst: bst.search(bst.min()),
    "max" : lambda bst: bst.max(),
    "maxdata" : lambda bst: bst.search(bst.max())
}
while True:
    cmd = input().split()
    fn = cmd[0]
    if not fn:
        break
    elif fn == "search":
        print(bst.search(int(cmd[1])))
    elif fn == "insert":
        print(bst.insert(int(cmd[1]), cmd[2]))
    elif fn == "remove":
        print(bst.remove(int(cmd[1])))
    else:
        print(func[fn](bst))
    print(bst.show())
