def solve(s):

    result = ''
    for x in s:
        small = result+chr(ord(x)-1)+'9'*(len(s)-len(result)-1)
        large = result+x*(len(s)-len(result))
        if int(large) > int(s):
            return int(small)
        else:
            result += x
    return int(result)

T = int(input())

for t in range(1, T+1):
    N = input()
    print ('Case #%d: %d' % (t, solve(N)))
