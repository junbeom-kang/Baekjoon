def solution(s):
    k = 0
    answer = ""
    while k < len(s):
        if 48 <= ord(s[k]) <= 57:
            answer += s[k]
            k += 1
        else:
            if s[k:k + 3] in dict3:
                answer += dict3[s[k:k + 3]]
                k += 3
            elif s[k:k + 4] in dict4:
                answer += dict4[s[k:k + 4]]
                k += 4
            else:
                answer += dict5[s[k:k + 5]]
                k += 5
    return answer
dict3={
    "one":"1","two":"2","six":"6"
}
dict4={
    "zero":"0","four":"4","five":"5","nine":"9"}

dict5={
    "three":"3","seven":"7","eight":"8"
}




