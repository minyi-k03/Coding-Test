
def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    
    
    for i in range(0,len(score),m):#분할
        basket=score[i:i+m]
            
        if len(basket)==m:
            answer+=min(basket)*m
    
    
        
        
            
    return answer
    