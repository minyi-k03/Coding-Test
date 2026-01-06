def solution(order):
    answer = 0
    
    order=str(order)
    
    for i in order:
        if i=="3":
            answer+=1
        elif i=="6":
            answer+=1
        elif i=="9":
            answer+=1
    
    
    
    return answer