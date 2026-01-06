def solution(n):
    answer = '수'
    
    for i in range(1,n):
        if i%2!=0:
            answer+='박'
        else:
            answer+='수'
    return answer