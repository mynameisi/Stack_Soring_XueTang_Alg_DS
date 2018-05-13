#!/usr/bin/python

n = int(raw_input())
R = map(int, raw_input().split(' '))


def sort(R):
    S = []
    t = R.pop()
    while True:
        if len(S) == 0 or (S[-1] <= t):
            S.append(t)
            if len(R) == 0:
                break
            t = R.pop()
        else:
            R.append(S.pop())
    return S


result = sort(R)
for i in range(n):
    print(result[i])
