import sys
input = sys.stdin.readline

## pos
#def rec(n, r, c):
#    r_pos, c_pos = r//(2**(n-1)), c//(2**(n-1))
#    pos = c_pos if r_pos==0 else c_pos+2
#
#    # escape
#    if n == 1:
#        return pos
#    return (2**(2*(n-1)))*pos + rec(n-1, r-(2**(n-1))*r_pos, c-(2**(n-1))*c_pos)


# short
def rec(n, r, c):
    if n == 0:
        return 0
    return 2*(r%2)+(c%2) + 4*rec(n-1, int(r/2), int(c/2))

n, r, c = map(int, input().split())
print(rec(n, r, c))
