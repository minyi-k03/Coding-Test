def solution(x):
    
    hashard=0
    x=str(x)
    
    for i in x:
        hashard+=int(i)
    
    if int(x)%hashard==0:
        return True
    
    return False