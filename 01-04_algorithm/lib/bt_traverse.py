import sys
from collections import deque
input = sys.stdin.readline

class node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class binary_tree():
    def __init__(self):
        self.root = None
    def preorder(self):
        self.ret = []
        def _preorder(node):
            if not node:
                return
            self.ret.append(node.data)
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
        return self.ret
    def inorder(self):
        self.ret = []
        def _inorder(node):
            if not node:
                return
            if node.left:
                _inorder(node.left)
            self.ret.append(node.data)
            if node.right:
                _inorder(node.right)
        _inorder(self.root)
        return self.ret
    def postorder(self):
        self.ret = []
        def _postorder(node):
            if not node:
                return
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            self.ret.append(node.data)
        _postorder(self.root)
        return self.ret
    def levelorder(self):
        self.ret = []
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            self.ret.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return self.ret

bt = binary_tree()
for i in range(1, 8):
    locals()["n"+str(i)] = node(i)
bt.root = n1
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7

print(bt.preorder())
print(bt.inorder())
print(bt.postorder())
print(bt.levelorder())
