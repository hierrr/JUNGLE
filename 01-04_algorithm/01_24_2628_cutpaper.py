import sys
input = sys.stdin.readline

w, h = map(int, input().split())
c = int(input())
cut_w, cut_h = [0, w], [0, h]
w_li, h_li = [], []

for _ in range(c):
    d, p = map(int, input().split())
    if d == 1:
        cut_w.append(p)
    else:
        cut_h.append(p)
cut_w.sort()
cut_h.sort()

for i in range(len(cut_w)-1):
    w_li.append(cut_w[i+1] - cut_w[i])
for j in range(len(cut_h)-1):
    h_li.append(cut_h[j+1] - cut_h[j])

print(max(w_li) * max(h_li))
