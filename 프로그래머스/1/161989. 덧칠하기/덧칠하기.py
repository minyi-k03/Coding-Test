#문제 이해가 어려웠음
def solution(n, m, section):
    answer = 0
    painted=0
    
    for i in section:
        if i>painted:
            painted=i+m-1 #핵심
            answer+=1
    
            
                
    
    
    return answer