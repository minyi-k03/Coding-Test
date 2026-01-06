def solution(N, stages):
    answer = []
    stages.sort()
    tmp={}
    all_people=len(stages)
    for i in range(1,N+1):
        if all_people!=0:
            fail_people=stages.count(i)
            tmp[i]=fail_people/all_people
            all_people-=fail_people
        else:
            tmp[i]=0
            
    
        
    
            
    
    return sorted(tmp,key=lambda x:tmp[x] ,reverse=True)