def solution(num_list, n):
    answer = []
    
    answer.append(num_list[:n])
    
    answer=sum(answer,[])
    
    return answer