def solution(str_list, ex):
    
    
    tmp=[s for s in str_list if ex not in s]
    
    answer="".join(tmp)
    return answer