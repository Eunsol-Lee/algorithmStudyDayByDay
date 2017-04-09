def solve(N, K):
    r = 1
    for i in range(61):
        minN = r - 1
        maxN = r*2 -1
        if K <= maxN:
            rest = N-maxN
            restC = rest // (r*2)
            restD = rest - restC*r*2
            K -= minN
            if restD <= r:
                if K <= restD:
                    return [restC+1, restC]
                else:
                    return [restC]*2
            restD -= r
            if restD <= r:
                if K <= restD:
                    return [restC+1]*2
                else:
                    return [restC+1, restC]

        r *= 2


T = int(input())

for i in range(1, T+1):
    N, K = [int(x) for x in input().split(' ')]
    l, r = solve(N, K)
    print ('Case #%d: %d %d' % (i, l, r))
