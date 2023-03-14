import sys
import itertools
input = sys.stdin.readline

li = []
for _ in range(9):
    li.append(int(input()))
rest = sum(li) - 100

twos = itertools.combinations(li, 2)
for two in twos:
    if sum(two) == rest:
        for one in two:
            li.remove(one)
        break

li.sort()
for i in li:
    print(i)
