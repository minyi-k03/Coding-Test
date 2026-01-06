def solution(a, d, included):
    answer=0
    lst=[]
    for i in range(len(included)):
        lst.append(a+(d*i))
        
    for idx,val in enumerate(included):
        if val:
            answer+=lst[idx]
            
    return answer