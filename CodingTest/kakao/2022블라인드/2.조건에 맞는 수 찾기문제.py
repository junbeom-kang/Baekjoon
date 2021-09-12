def solution(n, q):
    rev_base = ''

    while n > 0:
        print(n)
        n, mod = divmod(n, q)
    
        rev_base += str(mod)
    print()
    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력


print(solution(45, 3))