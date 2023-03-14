import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sch = list(map(int, input().split()))
pow = []
cnt = 0

for i, use in enumerate(sch):
    # already using
    if use in pow:
        continue
    # have place
    if len(pow) < n:
        pow.append(use)
    else:
        cnt += 1
        pow_i = 0
        tmp_i = -1
        # waiting schedule
        tmp = sch[i:]
        for j in pow:
            if j in tmp:
                # get idx of unpluging one, the last to use
                use_i = tmp.index(j)
                if tmp_i < use_i:
                    tmp_i = use_i
                    pow_i = j
            else:
                pow_i = j
                break
        pow[pow.index(pow_i)] = use
print(cnt)
