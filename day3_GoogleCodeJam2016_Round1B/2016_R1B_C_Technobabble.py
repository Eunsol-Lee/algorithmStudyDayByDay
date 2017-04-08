T = int(input())

def solve(v, g, n):
    f = [[0] * v for _ in range(v)]

    find = True
    while find:
        qu = [0]
        prev = [0] * v
        prev[0] = -1
        find = False
        while len(qu):
            t = qu.pop()
            if t == 1:
                find = True
                while t:
                    if g[prev[t]][t]:
                        f[prev[t]][t] += 1
                    else:
                        f[t][prev[t]] -= 1
                    t = prev[t]
                break

            for i in range(v):
                if not prev[i]:
                    if g[t][i] and not f[t][i]:
                        qu.insert(0, i)
                        prev[i] = t
                    if g[i][t] and f[i][t]:
                        qu.insert(0, i)
                        prev[i] = t
    s = 0



    for i in range(2, v):
        if f[i][1]:
            s+= 1


    return n-((v-2)- s)

for i in range(1, T + 1):
    N = int(input())
    g = [[0] * 2002 for _ in range(2002)]
    v = 2
    aList = []
    bList = []
    aIndex = []
    bIndex = []
    for j in range(N):
        A, B = input().split(' ')
        if not A in aList:
            aList.append(A)
            aIndex.append(v)
            g[0][v] = 1
            v += 1

        if not B in bList:
            bList.append(B)
            bIndex.append(v)
            g[v][1] = 1
            v+= 1

        g[aIndex[aList.index(A)]][bIndex[bList.index(B)]] = 1
    print ('Case #%d: %d' % (i, solve(v, g, N)))
