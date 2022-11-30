import sys
input = sys.stdin.readline

def dc(p, s, e):
    # distance between 2 points
    def dist(p1, p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    # escape
    if s == e:
        return sys.maxsize
    elif e-s == 1:
        return dist(p[s], p[e])
    # divide
    m = (s+e)//2
    d = min(dc(p, s, m), dc(p, m+1, e))
    # conquer
    # x axis
    pl = []
#    for i in range(s, e+1):
#        if (p[m][0]-p[i][0])**2 < d:
#            pl.append(p[i])
    for i in range(m, s-1, -1):
        if (p[m][0]-p[i][0])**2 < d:
            pl.append(p[i])
        else:
            break
    for j in range(m+1, e+1):
        if (p[m][0]-p[j][0])**2 < d:
            pl.append(p[j])
        else:
            break
    # y axis
    pl.sort(key=lambda x: x[1])
    l = len(pl)
    for i in range(l-1):
        for j in range(i+1, l):
            if (pl[i][1]-pl[j][1])**2 < d:
                d = min(d, dist(pl[i], pl[j]))
            else:
                break
    return d

n = int(input())
p = sorted(list(tuple(map(int, input().split())) for _ in range(n)))

print(dc(p, 0, n-1))
