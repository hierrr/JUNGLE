import sys
input = sys.stdin.readline

def rec(cut, row, col):
    global w, b
    tmp = 0
    for i in range(n//(2**cut)):
        for j in range(n//(2**cut)):
            tmp += li[row+i][col+j]
    # 0: white
    if tmp == 0:
        w += 1
    # 1: blue
    elif tmp == (n//(2**cut))**2:
        b += 1
    else:
        rec(cut+1, row, col)
        rec(cut+1, row+n//(2**(cut+1)), col)
        rec(cut+1, row, col+n//(2**(cut+1)))
        rec(cut+1, row+n//(2**(cut+1)), col+n//(2**(cut+1)))

# n = 2**(1~7)
n = int(input())
li = list(list(map(int, input().split())) for _ in range(n))
#w:0, b:1
w, b = 0, 0
rec(0, 0, 0)

print(f"{w}\n{b}")
