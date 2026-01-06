def solution(n):
    answer = 0
    lst=[]
    
    for i in range(2,n+1):
        for j in range(1,i+1):
            if i%j==0:
                lst.append(i)
                
        if lst.count(i)>=3:
            answer+=1
    
    
    return answer