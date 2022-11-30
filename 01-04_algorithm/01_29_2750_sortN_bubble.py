import sys
input = sys.stdin.readline

def bubble_sort(li):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

n = int(input())
li = [int(input()) for _ in range(n)]
bubble_sort(li)

print(*li, sep="\n")
