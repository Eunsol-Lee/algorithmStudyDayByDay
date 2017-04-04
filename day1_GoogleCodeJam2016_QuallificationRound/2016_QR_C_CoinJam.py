from itertools import combinations_with_replacement

def solve(N, J):
    pairs = 8
    zeros = N - 4 - pairs
    locations = combinations_with_replacement('01234', zeros)

    count = 0

    for result in locations:
        now = 0
        string = ''
        for i in range(zeros):
            while (now != int(result[i])):
                string += '11'
                now += 1
            string += '0'
        while (now < pairs / 2):
            now += 1
            string += '11'
        print ('11%s11 3 2 3 2 7 2 3 2 3' % (string))
        count += 1
        if (count == J):
            return

T = int(input())

for i in range(1,T+1):
    (N, J) = map(lambda x: int(x), input().split())
    print ('Case #%d:' % i)
    solve(N, J);
