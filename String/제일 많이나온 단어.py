import sys
input=sys.stdin.readline

def solution(S,L):
    def makeTable(P):
        lp = len(P)
        Table = [0] * lp
        i = 0
        for j in range(1, lp):
            while i > 0 and P[i] != P[j]:
                i = Table[i - 1]
            if P[i] == P[j]:
                i += 1
                Table[j] = i
        return Table

    def KMP(P, T):
        ans =0
        lt = len(T)
        lp = len(P)
        table = makeTable(P)
        i = 0
        for j in range(lt):
            while i > 0 and P[i] != T[j]:
                i = table[i - 1]
            if P[i] == T[j]:
                if i == lp - 1:
                    ans+=1
                    i = table[i]
                else:
                    i += 1
        return ans

    answer=0
    for i in L:
        answer=max(answer,KMP(i,S))
    print(answer)
    return

if __name__ == '__main__':
    S="BILLYBILLYBOO"
    L=["BILL", "MARIA", "LILLY"]
    solution(S,L)

