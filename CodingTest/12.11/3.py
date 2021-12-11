def solution(pixels):
    def check(arr):
        if arr[0]!='111':
            if arr[1]=='010':
                return '1'
            else:
                return '4'
        else:
            if arr[4]=='001':
                return '7'
            if arr[1]=='101':
                if arr[2]=='101':
                    return '0'
                else:
                    if arr[3]=='101':
                        return '8'
                    else:
                        return '9'
            elif arr[1]=='001':
                if arr[3]=='001':
                    return '3'
                else:
                    return '2'
            else:
                if arr[3]=='001':
                    return '5'
                else:
                    return '6'





    n=len(pixels[0])//3
    l=len(pixels[0])
    arr=[]
    answer = ''

    for i in range(5):
        temp=[]
        for j in range(l):
            temp.append(pixels[i][j])
        arr.append(temp)
    for i in range(n):
        answer+=check([row[i*3:i*3+3] for row in pixels[0:5]])
    print(answer)
    return answer

solution(["111111111111111111111111110111111111","001101001101101100101101010101001100","111101111101101111101111010111111111","100101100101101101101001010101001001","111111111111111111111111111111111111"])
solution(["110111101111111111110111","010101101100101101010100","010111111111101111010111","010001001001101101010001","111111001111111111111111"])
solution(["111110111101111101111101","100010101101001101100101","111010111111111111111111","001010101001100001001001","111111111001111001111001"])