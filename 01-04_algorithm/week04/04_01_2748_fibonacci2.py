import sys
input = sys.stdin.readline

## loop
#def fib(n):
#    pp, p = 0, 1
#    for i in range(n):
#        pp, p = p, pp + p
#    return pp

## rec
#def fib(n):
#    if n <= 1:
#        return n
#    return fib(n-1) + fib(n-2)

## tail rec
#def fib(n, p=1, pp=0):
#    if n <= 1:
#        return n * p
#    return fib(n-1, p+pp, p)

# dp
def fib(n):
    dp = [i for i in range(n+1)]
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input())
print(fib(n))
