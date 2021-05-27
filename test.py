def coin_pay(coins, m):
    if m > 0:
        while len(coins) > 0 and m < coins[0]:
            coins = coins[1:]  # 지불 금액보다 더 큰 단위의 동전 제외
        if coins[0] > 1:
            temp1=0,{}
            temp2=0,{}
            n1 = coin_pay(coins[1:], m)  # None대신 coins[0] 동전을 사용하지 않고 지불하는 경우 최소 코인 개수를 구하는 식 작성 함수 m값이 변하지 않는다
            # n1[0] 총 최소 코인 개수
            n2 = coin_pay(coins, m - coins[0])  # 튜플 (2,{5:1,1:1})

            if temp1[0]+n1[0]<temp2[0] + n2[0]+1:
                if coins[0] in n1[1]:
                    n1[1][coins[0]]+=1
                else:
                    temp1[1][coins[0]]=1
                temp1[1].update(n1[1])
                return n1[0],temp1[1]
            else:
                if coins[0] in n2[1]:
                    n2[1][coins[0]] += 1
                else:
                    temp2[1][coins[0]] = 1
                temp2[1].update(n2[1])
                return n2[0]+1,temp2[1]


        else:  # coins[0] == 1
            return m, {1: m}  # 총 m개의 동전이 필요하며 1짜리 동전 m개 사용해 지불

    else:  # m == 0
        return 0, {}  # 지불해야 할 금액이 0으로 없으므로 필요한 동전도 0개고 함께 빈 map을 타나태는 {}를 리턴

def run_coin_pay(coins,m):
    from time import perf_counter
    start = perf_counter()
    answer = coin_pay(coins,m)
    finish = perf_counter()
    print("coin_pay([",coins,",",m,") => ",answer,sep="")
    print(round(finish-start, ndigits=6), "seconds")

# 작성한 다음 아래 테스트를 돌려 보라
my_coins = [5,3,1]

run_coin_pay(my_coins,8)
print(my_coins)
run_coin_pay(my_coins,230)
#run_coin_pay(my_coins,280) # 대략 5초 이상 걸릴 것이다
#run_coin_pay(my_coins,330) # 이건 대략 10초 이상 걸릴 것이다
#run_coin_pay(my_coins,380) # 여기서부턴 너무 오래 걸려서 제대로 실행하기 힘들 것