def solve(s, k):
    s = '+'+s
    count = 0
    while True:
        q = s.find('+-')
        if q == -1:
            return str(count)
        count += 1
        if q+1+k>len(s):
            return 'IMPOSSIBLE'
        p = ''
        for x in s[q+1:q+1+k]:
            p += '+' if x == '-' else '-'
        s = s[:q+1]+p+s[q+1+k:]


T = int(input())
for t in range(1, T+1):
    S, k = input().split(' ')
    K = int(k)
    print ('Case #%d: %s' % (t, solve(S, K)))
