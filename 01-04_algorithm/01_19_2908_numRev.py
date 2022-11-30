import sys
input = sys.stdin.readline

a, b = input().split()
print(max(int(''.join(reversed(a))), int(''.join(reversed(b)))))
