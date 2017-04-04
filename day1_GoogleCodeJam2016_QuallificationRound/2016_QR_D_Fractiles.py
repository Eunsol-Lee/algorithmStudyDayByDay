T = int(input())

def solve(K, C, S):
    result = int((K+C-1)/C)
    if S < result:
        return "IMPOSSIBLE"
    else:
        now = 0
        text = ''
        for i in range(result):
            num = list(range(now + 1, now + 1 + C))
            num = list(map(lambda x: 1 if x > K else x, num))
            now += C
            value = 1
            for j in range(C):
                value += (num[j]-1)*(K**(C-j-1))
            text += str(value) + ' '
        return text

for i in range(1, T+1):
    (K, C, S) = map(lambda x: int(x), input().split())
    print('Case #%d: %s' % (i, solve(K, C, S)))
