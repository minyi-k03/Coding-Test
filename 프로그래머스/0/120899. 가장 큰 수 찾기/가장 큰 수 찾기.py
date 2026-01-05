def solution(array):
    answer = []
    max_num=max(array)
    max_index=array.index(max(array),0,len(array))
    
    
    answer.append(max_num)
    answer.append(max_index)
    
    
    
    return answer