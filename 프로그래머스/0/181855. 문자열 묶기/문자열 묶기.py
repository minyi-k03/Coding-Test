def solution(strArr):
    answer = []
    str_len=[]
    
    for i in strArr:
        str_len.append(len(i))
    
    for i in set(str_len):
        answer.append(str_len.count(i))
    
    
    
    return max(answer)