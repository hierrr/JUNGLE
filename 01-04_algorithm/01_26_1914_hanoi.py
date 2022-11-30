import sys
input = sys.stdin.readline

def hanoi(n, start, dest, via):
    if n == 1:
        print(start, dest)
        return
    # start > via
    hanoi(n-1, start, via, dest)
    print(start, dest)
    # via > dest
    hanoi(n-1, via, dest, start) 

n = int(input())
print(2 ** n-1)

if n <= 20:
    # n, start, dest, via
    hanoi(n, 1, 3, 2)
