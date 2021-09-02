def solution(s):
    ls=len(s)
    i=0
    answer=""
    while i<ls:
        print(s[i])
        if ord('a')<=ord(s[i])<=ord('z'):
            if s[i:i+3] in d3:
                answer+=d3[s[i:i+3]]
                i+=3
            elif s[i:i+4] in d4:
                answer+=d4[s[i:i+4]]
                i+=4
            else:
                answer+=d5[s[i:i+5]]
                i+=5
        else:
            answer+=s[i]
            i+=1
    answer=int(answer)
    return answer

d3 = {"one":"1","two":"2","six":"6"}
d4 = {"zero":"0","four":"4","five":"5","nine":"9"}
d5={"three":"3","seven":"7","eight":"8"}
if __name__ == '__main__':
    print(solution("one4seveneight"))