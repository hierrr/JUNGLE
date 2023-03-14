import sys
input = sys.stdin.readline

words = [input().rstrip() for _ in range(int(input()))]
words = list(set(words))
words.sort(key=lambda i: (len(i), i))

print(*words, sep="\n")
