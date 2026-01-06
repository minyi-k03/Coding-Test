def solution(x1, x2, x3, x4):
    answer=False
    if(x1+x2) and (x3+x4) >=1:
        answer=True
    elif(x1+x2) or (x3+x4):
        answer=False
    elif(x1+x2) and (x3+x4):
        answer=False
    
    return answer