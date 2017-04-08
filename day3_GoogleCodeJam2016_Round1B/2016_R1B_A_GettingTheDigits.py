def solve(S):
    alp = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
    count = [['Z', 'W', 'U', 'X', 'G'], ['O', 'T', 'F', 'S'], ['I']]
    countIndex = [[0, 2, 4, 6, 8], [1, 3, 5, 7], [9]]
    letters = [0] * 26
    result = [0] * 10
    final = ''
    for x in S:
        letters[ord(x) - ord('A')] += 1
    for i in range(len(count)):
        for x, y in zip(count[i], countIndex[i]):
            val = letters[ord(x) - ord('A')]
            result[y] = val
            for z in alp[y]:
                letters[ord(z) - ord('A')] -= val
    for i in range(len(result)):
        final += chr(ord('0') + i) * result[i]
    return final


T = int(input())

for i in range(1, T+1):
    S = input()
    print('Case #%d: %s' % (i, solve(S))
