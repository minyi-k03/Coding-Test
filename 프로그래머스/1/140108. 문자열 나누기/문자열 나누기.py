def solution(s):
    answer = 0
    lst=[]
    count=0
    count2=0
    
    for i in s:
        if count==count2:
            answer+=1
            k=i
        if k==i:
            count+=1
        else:
            count2+=1
                
        
    
    return answer