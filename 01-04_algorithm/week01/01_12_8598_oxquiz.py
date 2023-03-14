import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    case = input()
    score, count = 0, 0
    for i in case:
        if i == "O":
            count += 1
            score += count
        else:
            count = 0
    print(score)
