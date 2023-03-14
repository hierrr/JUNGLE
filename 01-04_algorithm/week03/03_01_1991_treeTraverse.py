import sys
input = sys.stdin.readline

# implement binary tree
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

n = int(input())
nl = []
for i in range(26):
    nl.append(node(chr(i+ord("A"))))
bt = binary_tree()
bt.root = nl[0]
for _ in range(n):
    p, l, r = input().split()
    np = nl[ord(p)-ord("A")]
    if l != ".":
        np.left = nl[ord(l)-ord("A")]
    if r != ".":
        np.right = nl[ord(r)-ord("A")]

print("".join(bt.preorder()))
print("".join(bt.inorder()))
print("".join(bt.postorder()))

## dict
#def preorder(node):
#    if node == ".":
#        return
#    print(node, end="")
#    preorder(tree[node][0])
#    preorder(tree[node][1])
#def inorder(node):
#    if node == ".":
#        return
#    inorder(tree[node][0])
#    print(node, end="")
#    inorder(tree[node][1])
#def postorder(node):
#    if node == ".":
#        return
#    postorder(tree[node][0])
#    postorder(tree[node][1])
#    print(node, end="")
#
#n = int(input())
#tree = {}
#for _ in range(n):
#    np, nl, nr = input().split()
#    tree[np] = [nl, nr]
#
#preorder("A")
#print()
#inorder("A")
#print()
#postorder("A")
