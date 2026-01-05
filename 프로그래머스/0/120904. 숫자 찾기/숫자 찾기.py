def solution(num, k):
    answer = 0
    num=str(num)
    k=str(k)
    for idx, val in enumerate(num):
        
        if k==val:
            return idx+1
            
        
        
        
    return -1