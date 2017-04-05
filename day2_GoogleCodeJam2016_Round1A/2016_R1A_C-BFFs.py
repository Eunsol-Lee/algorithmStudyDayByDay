def solve(N, F):
    m = 0
    circle = [0] * N
    linear = [0] * N
    linearFinal = [0] * N
    linearCount = 0
    for i in range(N):
        now = i
        count = 0
        visited = [0] * N
        visited[now] = 1
        while True:
            count += 1
            visited[now] = count
            now = F[now]
            if visited[now]:
                if now == i:
                    circle[i] = count
                else:
                    linear[i] = visited[now]-1
                    linearFinal[i] = now
                break;
    for i in range(N):
        m = max(m, circle[i])
        if circle[i] == 2:
            l = 0
            r = 0
            for j in range(N):
                if linearFinal[j] == i:
                    l = max(l, linear[j])
                if linearFinal[j] == F[i]:
                    r = max(r, linear[j])
            linearCount += l + r + 2


    return max(m, linearCount/2)







T = int(input())

for i in range(1, T+1):
    N = int(input())
    F = [int(x)-1 for x in input().split()]
    print ('Case #%d: %d' % (i, solve(N, F)))
