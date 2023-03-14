import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def post(tree):
    if len(tree) <= 1:
        return tree
    for i in range(len(tree)):
        # root: tree[0]
        if tree[i] > tree[0]:
            # root + left + right >> left + right + root
            return post(tree[1:i]) + post(tree[i:]) + [tree[0]]
    return post(tree[1:]) + [tree[0]]

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break
print(*post(tree), sep="\n")
