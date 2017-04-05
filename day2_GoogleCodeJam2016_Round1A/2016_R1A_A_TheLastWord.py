def solve(S):
    now = ''
    result = ''
    for x in S:
        if now <= x:
            result = x + result
            now = x
        else:
            result = result + x
    return result

T = int(input())

for i in range(1, T+1):
    S = input()
    print('Case #%d: %s' % (i, solve(S)))
