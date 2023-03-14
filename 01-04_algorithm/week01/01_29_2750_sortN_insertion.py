import sys
input = sys.stdin.readline

def insertion_sort(li):
    for i in range(1, len(li)):
        key = li[i]
        j = i
        while j > 0 and li[j-1] > key:
            li[j] = li[j-1]
            j -= 1
        li[j] = key

n = int(input())
li = [int(input()) for _ in range(n)]
insertion_sort(li)

print(*li, sep="\n")
