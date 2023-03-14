import sys
input = sys.stdin.readline

li = []

for i in range(9):
    li.append(int(input()))

m = max(li)

print(m)
print(li.index(m)+1)
