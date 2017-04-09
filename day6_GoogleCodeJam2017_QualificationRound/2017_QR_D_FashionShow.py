def solve(n, mat):
    dic = '.+xo'
    result = {'result': [0, 0], 'indivi': []}
    # find bishop
    r = [0] * n
    c = [0] * n
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 2 or mat[i][j] == 3:
                r[i] = 1
                c[j] = 1
    for i in range(n):
        if r[i] == 0:
            for j in range(n):
                if c[j] == 0:
                    r[i] = 1
                    c[j] = 1
                    mat[i][j] = 2 if not mat[i][j] else 3
                    result['result'][1] += 1
                    result['indivi'].append('%s %d %d'%( dic[mat[i][j]], i+1, j+1))
                    break

    # find rook
    pDia = [0] * (2 * n)
    mDia = [0] * (2 * n)

    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1 or mat[i][j] == 3:
                pDia[i+j] = 1
                mDia[i-j+n] = 1

    for i in range(n*2-1):
        if i % 2 == 0:
            plus = i // 2
        else:
            plus = (n-1)*2 - i//2
        for j in range(n*2):
            r = j
            c = plus-r
            if r >=0 and c >=0 and r <n and c< n :
                if not pDia[r+c] and not mDia[r-c+n]:
                    pDia[r+c] = 1
                    mDia[r-c+n] = 1
                    mat[r][c] = 1 if not mat[r][c] else 3
                    if mat[r][c] == 3 and '%s %d %d' % ('x', r+1, c+1) in result['indivi']:
                        result['indivi'][result['indivi'].index('%s %d %d' % ('x', r+1, c+1))] = '%s %d %d' %( dic[mat[r][c]], r+1, c+1)
                    else:
                        result['result'][1] += 1
                        result['indivi'].append('%s %d %d' %( dic[mat[r][c]], r+1, c+1))
                    break

    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1 or mat[i][j] == 2:
                result['result'][0] += 1
            elif mat[i][j] == 3:
                result['result'][0] += 2


    return result

dic = {'.': 0, '+': 1, 'x': 2, 'o': 3}
T = int(input())
for t in range(1, T+1):
    N, M = [int(x) for x in input().split(' ')]
    mat = [[0] * N for _ in range(N)]
    for m in range(M):
        p, x, y = input().split(' ')
        mat[int(x)-1][int(y)-1] = dic[p]
    result = solve(N, mat)
    print ('Case #%d: %d %d' % (t, result['result'][0], result['result'][1]))
#    for x in result['indivi']:
#        print(x)
