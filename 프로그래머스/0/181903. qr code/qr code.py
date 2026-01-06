def solution(q, r, code):
    answer = ''
    calculate=[]
    
    for idx, val in enumerate(code):
        if idx%q==r:
            answer+=val
            
    
    return answer