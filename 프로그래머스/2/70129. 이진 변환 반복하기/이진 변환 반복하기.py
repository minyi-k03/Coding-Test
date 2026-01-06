def solution(s):
    answer = []
    zero_count=0
    turn_count=0
    while s!="1":
        for i in s:
            if i=="0":
                s=s.replace(i,"")
                zero_count+=1
               
        s=format(len(s),'b')
        turn_count+=1
        
        
    
    answer.append(turn_count)
    answer.append(zero_count)
    
    
    
    
    
        
    
    
    
    return answer