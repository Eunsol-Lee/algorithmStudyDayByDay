
def commonEval(A, B):
    global minimal, lindex, rindex
    a = int(A)
    b = int(B)
    d = abs(a-b)
    if minimal > d:
        minimal = d
        lindex = A
        rindex = B
    if minimal == d:
        if a < int(lindex):
            lindex = A
            rindex = B
        if a == int(lindex):
            if b < int(rindex):
                lindex = A
                rindex = B

def leftEval(A, B, p):
    A = A.replace('?', '0')
    B = B.replace('?', '9')
    commonEval(A, B)

def rightEval(A, B, p):
    A = A.replace('?', '9')
    B = B.replace('?', '0')
    commonEval(A, B)


def solve(A, B, p):
    if p == len(A):
        commonEval(A, B)
        return
    if A[p] == '?' and B[p] == '?':
        leftEval(A[:p]+'1'+A[p+1:], B[:p]+'0'+B[p+1:], p+1)
        rightEval(A[:p]+'0'+A[p+1:], B[:p]+'1'+B[p+1:], p+1)
        A = A[:p]+'0'+A[p+1:]
        B = B[:p]+'0'+B[p+1:]
        solve(A, B, p+1)
        return
    if A[p] == '?':
        n = ord(B[p])
        if n != ord('9'):
            leftEval(A[:p]+chr(n+1)+A[p+1:], B, p+1)
        if n != ord('0'):
            rightEval(A[:p]+chr(n-1)+A[p+1:], B, p+1)
        A = A[:p]+B[p]+A[p+1:]
        solve(A, B, p+1)
        return
    if B[p] == '?':
        n = ord(A[p])
        if n != ord('9'):
            rightEval(A, B[:p]+chr(n+1)+B[p+1:], p+1)
        if n != ord('0'):
            leftEval(A, B[:p]+chr(n-1)+B[p+1:], p+1)
        B = B[:p]+A[p]+B[p+1:]
        solve(A, B, p+1)
        return
    if A[p] > B[p]:
        leftEval(A, B, p+1)
        return
    if A[p] < B[p]:
        rightEval(A, B, p+1)
        return
    solve(A, B, p+1)


T = int(input())
for i in range(1, T+1):

    minimal = 10 ** 20
    lindex = str(10**20)
    rindex = str(10**20)

    C, J = input().split(' ')
    solve(C, J, 0)
    print('Case #%d: %s %s' % (i, lindex, rindex))
