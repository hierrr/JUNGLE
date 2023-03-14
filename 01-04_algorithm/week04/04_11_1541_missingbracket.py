import sys
input = sys.stdin.readline

# short
#a = [sum([int(i) for i in sp.split('+')]) for sp in input().split('-')]
#print(a[0] - sum(a[1:]))

a = input().split('-')
s = 0
for i in a[0].split('+'):
    s += int(i)
for j in a[1:]:
    for k in j.split('+'):
        s -= int(k)
print(s)
