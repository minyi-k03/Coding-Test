def solution(board, moves):
    answer = 0
    basket=[]
    
    
    for i in moves: #인형을 뽑아서 basket 디큐에 넣는 코드 성공함
        for j in range(len(board)):
            if board[j][i-1]!=0:
                basket.append(board[j][i-1])
                board[j][i-1]=0
                
            
                if len(basket)>1:
                    if basket[-1]==basket[-2]:
                        basket.pop(-1)
                        basket.pop(-1)
                        answer+=2
                break
    return answer