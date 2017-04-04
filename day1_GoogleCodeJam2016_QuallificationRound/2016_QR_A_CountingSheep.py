def solve(N):
    num = [0] * 10;
    numCount = 0
    if N == 0:
        return 'INSOMNIA'
    for i in range(1,1000):
        p = i * N
        while (p):
            m = p % 10
            if num[m] == 0:
                num[m] = 1
                numCount += 1
            p = int(p / 10)
        if numCount == 10:
            return str(i * N)

T = int(input())

for i in range(1,T+1):
    N = int(input())
    print ('Case #%d: %s' % (i, solve(N)))
