import sys
from collections import deque
input = sys.stdin.readline
# input
n = int(input())
brd = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    ar, ac = map(int, input().split())
    brd[ar-1][ac-1] = 2
cd = dict()
l = int(input())
for _ in range(l):
    x, c = input().split()
    cd[int(x)] = c
# set
sec = 0
sr, sc = 0, 0
brd[sr][sc] = 1
d = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
queue = deque()
queue.append((sr, sc))
# play
while True:
    sec += 1
    sr += dr[d]
    sc += dc[d]
    # escape: hits a wall or its own body
    if not (0<=sr<n and 0<=sc<n) or brd[sr][sc] == 1:
        break
    # eat apple
    if brd[sr][sc] == 2:
        brd[sr][sc] = 1
        queue.append((sr, sc))
    else:
        brd[sr][sc] = 1
        queue.append((sr, sc))
        tr, tc = queue.popleft()
        brd[tr][tc] = 0
    # turn levo or dextro
    if sec in cd:
        if cd[sec] == "L":
            d = (d-1)%4
        else:
            d = (d+1)%4
# fin
print(sec)
