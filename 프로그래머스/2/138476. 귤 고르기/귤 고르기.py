def solution(k, tangerine):
    answer = 0
    quantity = 0
    
    tangerine_dict = {} #크기:개수
    
    tangerine.sort()
    
    for i in tangerine:
        if i not in tangerine_dict:
            tangerine_dict[i] = 1
        else:
            tangerine_dict[i]+=1
    
    tangerine_list = sorted(tangerine_dict.items(), key=lambda x:x[1],reverse=True)
    
    for i in tangerine_list:
        
        if quantity >= k:
            return answer
            break
        else:
            quantity += i[1]
            answer += 1
        
        
        
        
    
    
    
    
    
    return answer