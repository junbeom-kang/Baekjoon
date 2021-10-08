import sys

input = sys.stdin.readline


def solution():
    def makeTable(pattern):
        lp = len(pattern)
        table = [0] * lp
        i = 0
        for j in range(1, lp):
            while i > 0 and pattern[i] != pattern[j]:
                i = table[i - 1]
            if pattern[i] == pattern[j]:
                i += 1
                table[j] = i
        return table

    def kmp(S, P):
        table = makeTable(P)
        i = 0
        ls, lp = len(S), len(table)
        for j in range(ls):
            while i > 0 and P[i] != S[j]:
                i = table[i - 1]
            if P[i] == S[j]:
                if i == lp - 1:
                    return 1
                else:
                    i+=1
        return 0

    string = []
    for i in s:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            string.append(i)
    str = ''.join(string)
    print(kmp(str, pattern))

    return


if __name__ == '__main__':
    s = input().rstrip()
    pattern = input().rstrip()
    solution()
