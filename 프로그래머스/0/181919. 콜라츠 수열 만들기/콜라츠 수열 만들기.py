def solution(n):
    answer=[]
    while n!=1:
        answer.append(int(n))
        if(n%2==0):
            n=n/2
        elif(n%2!=0):
            n=3*n+1
    answer.append(1)        
    
    return answer