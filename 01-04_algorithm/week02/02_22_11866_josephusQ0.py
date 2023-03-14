import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])
r = []
while queue:
    queue.rotate(-(k-1))
    r.append(str(queue.popleft()))
print("<"+", ".join(r)+">")
