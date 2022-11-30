import sys
input = sys.stdin.readline

def pow_mat(m, e):
    # conquer
    def pow_op(m1, m2):
        tmp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                t = 0
                for k in range(n):
                    t += m1[i][k] * m2[k][j]
                tmp[i][j] = t % 10**3
        return tmp
    # escape
    if e == 1:
        for i in range(n):
            for j in range(n):
                m[i][j] %= 10**3
        return m
    # divide
    if e%2:
        return pow_op(pow_mat(m, e-1), pow_mat(m, 1))
    else:
        tmp = pow_mat(m, e//2)
        return pow_op(tmp, tmp)

n, b = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))

ans = pow_mat(a, b)
for a in ans:
    print(*a)
