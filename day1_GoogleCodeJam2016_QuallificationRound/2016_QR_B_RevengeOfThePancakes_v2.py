def solve(S):
    S += '+'
    return S.count('-+')+S.count('+-')

T = int(input())

for i in range(1,T+1):
    S = input()
    print ('Case #%d: %s' % (i, solve(S)))
