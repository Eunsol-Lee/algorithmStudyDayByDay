def solve(N, List):
    List.append(2501)
    count = 0
    now = 0
    result = ''
    for x in List:
        if now != x:
            if count % 2 == 1:
                result += str(now) + ' '
            count = 1
            now = x
        else:
            count += 1
    return result

T = int(input())

for i in range(1, T+1):
    N = int(input())
    List = [0] * N * (N*2-1)
    for j in range(N*2-1):
        inp = [int(x) for x in input().split()]
        for k in range(N):
            List[j*N-N+k]=inp[k]
    print ('Case #%d: %s' % (i, solve(N, sorted(List))))
