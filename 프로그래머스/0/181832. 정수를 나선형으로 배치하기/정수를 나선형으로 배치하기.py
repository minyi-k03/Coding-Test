def solution(n):
    answer = [[0 for _ in range(n)]for _ in range(n)]
    col=0 #세로 #i
    row=-1 #가로 #j
    reverse=1
    row_size=n # 가로 길이
    col_size=n #세로 길이
    count=1
    invert=True
    
    while row_size and col_size:
        for _ in range(row_size):
            row+=reverse
            answer[col][row]=count
            count+=1
        
        col_size-=1
        
        for _ in range(col_size):
            col+=reverse
            answer[col][row]=count
            count+=1
            
        row_size-=1
        
        reverse=-reverse
    
    
    return answer