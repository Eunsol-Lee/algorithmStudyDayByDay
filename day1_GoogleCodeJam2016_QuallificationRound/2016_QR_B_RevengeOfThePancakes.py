def solve(S):
    S += '+'
    count = 0
    while (len(S)*'+' != S):
        count += 1
        if S[0] == '-':
            index = S.index('+')
            S = index * '+' + S[index:]
        else:
            index = S.index('-')
            S = index * '-' + S[index:]
    return count

T = int(input())

for i in range(1,T+1):
    S = input()
    print ('Case #%d: %s' % (i, solve(S)))
