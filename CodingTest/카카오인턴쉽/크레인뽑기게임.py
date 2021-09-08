def solution(board, moves):
    answer = 0
    stack=[]
    high=len(board)
    width=len(board[0])
    arr=[[]for _ in range(width)]
    for i in range(high-1,-1,-1):
        for j in range(width):
            if board[i][j]:
                arr[j].append(board[i][j])
    print(arr)
    for i in moves:
        if arr[i-1]:
            stack.append(arr[i-1].pop())
            if len(stack)>1:
                if stack[-1]==stack[-2]:
                    print(stack)
                    stack.pop()
                    stack.pop()
                    answer+=1
    return answer*2