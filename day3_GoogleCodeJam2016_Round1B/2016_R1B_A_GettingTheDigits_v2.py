import numpy as np

def solve(S):
    alp = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

    A = np.zeros((26, 10))
    for i in range(10):
        for x in alp[i]:
            A[ord(x)-ord('A'), i] += 1

    B = np.zeros(26)
    for x in S:
        B[ord(x)-ord('A')] += 1

    X = np.linalg.lstsq(A, B)[0]
    final = ''
    for i in range(10):
        final += chr(ord('0')+i)*int(round(X[i]))

    return final


T = int(input())

for i in range(1, T+1):
    S = input()
    print('Case #%d: %s' % (i, solve(S)))
