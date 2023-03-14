import sys
input = sys.stdin.readline

def grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score:
        return "B"
    elif 70 <= score:
        return "C"
    elif 60 <= score:
        return "D"
    else:
        return "F"

print(grade(int(input())))