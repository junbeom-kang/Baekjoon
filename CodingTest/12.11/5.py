def solution(strs):
    def check(str):
        can=False
        l=len(str)
        if l<3:
            return
        if str[0]=='A':
            state=0
        else:
            state=1
        i=0
        while i<l:
            if state==0:
                if str[i:i+3]!="AAB":
                    can=False
                    break
                else:
                    can=True
                    i+=3
                    while i<l and str[i]=="B":
                        can=True
                        i+=1
                    if i>l-1:
                        break
                    can=False
                    if i<l-1 and str[i]=='A':
                        if str[i+1]!='A':
                            state=1
                            i-=1
            elif state==1:
                if i+2<l:
                    if str[i:i+3]=="BAB":
                        i+=3
                    while i<l and str[i]=="B":
                        i+=1
                    if i>l-1:
                        break
                    else:
                        if str[i]=='A':
                            if i+1==l:
                                can=True
                            else:
                                if str[i+1]=='A':
                                    state=0
                                else:
                                    state=1
                                i+=1
                else:
                    break

        if can:
            return True
        else:
            return False

    answer = 0
    for i in strs:
        if check(i):
            answer+=1
    print(answer)
    return answer

#solution(["AABAAA"])
solution(["BA"])